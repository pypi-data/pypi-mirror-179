#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module containing all import/export functionalities.
"""
import logging
import os
import shutil
import time
from pathlib import Path
from tempfile import TemporaryDirectory

import numpy as np
import xarray as xr
from numpy import asarray, concatenate, ones_like, zeros_like
from tqdm import tqdm

logger = logging.getLogger(__name__)


ufunc_kwargs = dict(vectorize=True)
concat_dim = "_concat_dim"
concat_kwargs = dict(dim=concat_dim, coords="minimal")


# IO functions
def int_to_str(arr):
    """
    Convert numpy array to str typed array.
    """
    convert = np.frompyfunc(lambda i: "%i" % i, 1, 1)
    return convert(arr)


def float_to_str(arr, ensure_sign=True):
    """
    Convert numpy array to str typed array.
    """
    if ensure_sign:
        convert = np.frompyfunc(lambda f: "%+f" % f, 1, 1)
    else:
        convert = np.frompyfunc(lambda f: "%f" % f, 1, 1)
    return convert(arr)


def fill_by(target_shape, where, fill, other=""):
    """
    Create array of `target_shape` with values from `fill` where `where` is
    True.
    """
    res = np.full(target_shape, other).astype(object)
    res[where] = fill
    return res


def objective_to_file(m, f, log=False):
    """
    Write out the objective of a model to a lp file.
    """
    if log:
        logger.info("Writing objective.")

    f.write("min\n\nobj:\n\n")
    coeffs = m.objective.coeffs.values
    vars = m.objective.vars.values
    nnz = vars != -1
    coeffs, vars = coeffs[nnz], vars[nnz]

    if np.isnan(coeffs).any():
        raise ValueError(
            "Objective coefficients are missing (nan) where variables are not (-1)."
        )

    objective = float_to_str(coeffs) + " x" + int_to_str(vars)
    f.write("\n".join(objective))
    del objective


def constraints_to_file(m, f, log=False):
    """
    Write out the constraints of a model to a lp file.
    """
    f.write("\n\ns.t.\n\n")
    m.constraints.sanitize_missings()
    kwargs = dict(broadcast_like="vars", filter_missings=True)
    vars = m.constraints.iter_ravel("vars", **kwargs)
    coeffs = m.constraints.iter_ravel("coeffs", **kwargs)
    labels = m.constraints.iter_ravel("labels", **kwargs)

    labels_ = m.constraints.iter_ravel("labels", filter_missings=True)
    sign_ = m.constraints.iter_ravel("sign", filter_missings=True)
    rhs_ = m.constraints.iter_ravel("rhs", filter_missings=True)

    iterate = zip(labels, vars, coeffs, labels_, sign_, rhs_)
    if log:
        iterate = tqdm(iterate, "Writing constraints.", len(m.constraints.labels))

    for (l, v, c, l_, s_, r_) in iterate:

        if not c.size:
            continue

        diff_con = l[:-1] != l[1:]
        new_con_b = concatenate([asarray([True]), diff_con])
        end_of_con_b = concatenate([diff_con, asarray([True])])

        l = fill_by(v.shape, new_con_b, "\nc" + int_to_str(l_) + ":\n")
        s = fill_by(v.shape, end_of_con_b, "\n" + s_.astype(object) + "\n")
        r = fill_by(v.shape, end_of_con_b, float_to_str(r_, ensure_sign=False))
        constraints = l + float_to_str(c) + " x" + int_to_str(v) + s + r

        f.write("\n".join(constraints))
        f.write("\n")
        del l, s, r, constraints


def bounds_to_file(m, f, log=False):
    """
    Write out variables of a model to a lp file.
    """
    f.write("\n\nbounds\n\n")
    lower = m.non_binaries.iter_ravel("lower", filter_missings=True)
    upper = m.non_binaries.iter_ravel("upper", filter_missings=True)
    labels = m.non_binaries.iter_ravel("labels", filter_missings=True)

    iterate = zip(lower, labels, upper)
    if log:
        iterate = tqdm(iterate, "Writing variables.", len(m.non_binaries.labels))

    for (lo, l, up) in iterate:

        if not l.size:
            continue

        bounds = float_to_str(lo) + " <= x" + int_to_str(l) + " <= " + float_to_str(up)
        f.write("\n".join(bounds))
        f.write("\n")
        del bounds


def binaries_to_file(m, f, log=False):
    """
    Write out binaries of a model to a lp file.
    """
    f.write("\n\nbinary\n\n")
    labels = m.binaries.iter_ravel("labels", filter_missings=True)

    if len(m.variables._binary_variables) == 0:
        return

    iterate = labels
    if log:
        iterate = tqdm(iterate, "Writing binaries.", len(m.binaries.labels))

    for l in iterate:

        if not l.size:
            continue

        bounds = "x" + int_to_str(l)
        f.write("\n".join(bounds))
        f.write("\n")
        del bounds


def to_file(m, fn):
    """
    Write out a model to a lp file.
    """
    fn = m.get_problem_file(fn)

    if os.path.exists(fn):
        os.remove(fn)  # ensure a clear file

    log = m._xCounter > 10000

    with open(fn, mode="w") as f:

        start = time.time()

        objective_to_file(m, f, log)
        constraints_to_file(m, f, log)
        bounds_to_file(m, f, log)
        binaries_to_file(m, f, log)
        f.write("end\n")

        logger.info(f" Writing time: {round(time.time()-start, 2)}s")

    return fn


def to_gurobipy(m):
    """
    Export the model to gurobipy.

    This function does not write the model to intermediate files but directly
    passes it to gurobipy. Note that for large models this is not
    computationally efficient.

    Parameters
    ----------
    m : linopy.Model

    Returns
    -------
    model : gurobipy.Model
    """
    import gurobipy

    m.constraints.sanitize_missings()
    model = gurobipy.Model()

    M = m.matrices

    names = "x" + M.vlabels.astype(str).astype(object)
    kwargs = {}
    if len(m.binaries.labels):
        kwargs["vtype"] = M.vtypes
    x = model.addMVar(M.vlabels.shape, M.lb, M.ub, name=list(names), **kwargs)

    model.setObjective(M.c @ x)

    names = "c" + M.clabels.astype(str).astype(object)
    c = model.addMConstr(M.A, x, M.sense, M.b)
    c.setAttr("ConstrName", list(names))

    model.update()
    return model


def to_highspy(m):
    """
    Export the model to highspy.

    This function does not write the model to intermediate files but directly
    passes it to highspy.

    Note, this function does not track variable and constraint labels.

    Parameters
    ----------
    m : linopy.Model

    Returns
    -------
    model : highspy.Highs
    """
    import highspy

    M = m.matrices
    h = highspy.Highs()
    h.addVars(len(M.vlabels), M.lb, M.ub)
    if len(m.binaries.labels):
        vtypes = M.vtypes
        blabels = np.arange(len(vtypes))[vtypes == "B"]
        nbinaries = len(blabels)
        h.changeColsIntegrality(nbinaries, blabels, ones_like(blabels))
        h.changeColsBounds(nbinaries, blabels, zeros_like(blabels), ones_like(blabels))
    h.changeColsCost(len(M.c), np.arange(len(M.c), dtype=np.int32), M.c)
    A = M.A.tocsr()
    num_cons = A.shape[0]
    lower = np.where(M.sense != "<", M.b, -np.inf)
    upper = np.where(M.sense != ">", M.b, np.inf)
    h.addRows(num_cons, lower, upper, A.nnz, A.indptr, A.indices, A.data)
    return h


def to_block_files(m, fn):
    """
    Write out the linopy model to a block structured output.
    """
    if fn is None:
        fn = TemporaryDirectory(prefix="linopy-problem-", dir=m.solver_dir).name

    path = Path(fn)
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(exist_ok=True)

    m.calculate_block_maps()

    N = int(m.blocks.max())
    for n in range(N + 2):
        (path / f"block{n}").mkdir()

    vars = m.variables
    cons = m.constraints

    # Write out variables
    blocks = vars.ravel("blocks", filter_missings=True)
    for key, suffix in zip(["labels", "lower", "upper"], ["x", "xl", "xu"]):
        arr = vars.ravel(key, filter_missings=True)
        for n in tqdm(range(N + 1), desc=f"Write variable {key}"):
            arr[blocks == n].tofile(path / f"block{n}" / suffix, sep="\n")

    # Write out objective (uses variable blocks from above)
    coeffs = np.zeros(m._xCounter)
    coeffs[np.asarray(m.objective.vars)] = np.asarray(m.objective.coeffs)
    # reorder like non-missing variables
    coeffs = coeffs[vars.ravel("labels", filter_missings=True)]
    for n in tqdm(range(N + 1), desc="Write objective"):
        coeffs[blocks == n].tofile(path / f"block{n}" / "c", sep="\n")

    # Write out rhs
    blocks = cons.ravel("blocks", filter_missings=True)
    rhs = cons.ravel("rhs", filter_missings=True)
    is_equality = cons.ravel(cons.sign == "=", filter_missings=True)
    is_lower_bound = cons.ravel(cons.sign == ">=", filter_missings=True)

    for n in tqdm(range(N + 2), desc="Write RHS"):
        is_blockn = blocks == n

        rhs[is_blockn & is_equality].tofile(path / f"block{n}" / "b", sep="\n")

        not_equality = is_blockn & ~is_equality
        is_lower_bound_sub = is_lower_bound[not_equality]
        rhs_sub = rhs[not_equality]

        lower_bound = np.where(is_lower_bound_sub, rhs_sub, -np.inf)
        lower_bound.tofile(path / f"block{n}" / "dl", sep="\n")

        upper_bound = np.where(~is_lower_bound_sub, rhs_sub, np.inf)
        upper_bound.tofile(path / f"block{n}" / "du", sep="\n")

    # Write out constraints
    conblocks = cons.ravel("blocks", "vars", filter_missings=True)
    varblocks = cons.ravel("var_blocks", "vars", filter_missings=True)
    is_equality = cons.ravel(cons.sign == "=", "vars", filter_missings=True)

    is_varblock_0 = varblocks == 0
    is_conblock_L = conblocks == N + 1

    keys = ["labels", "coeffs", "vars"]

    def filtered(arr, mask, key):
        """
        Set coefficients to zero for mask, keep others unchanged.

        PIPS requires this information to set the shape of sub-matrices.
        """
        assert key in keys
        if key == "coeffs":
            return np.where(mask, arr, 0)
        return arr

    for key, suffix in zip(keys, ["row", "data", "col"]):
        arr = cons.ravel(key, "vars", filter_missings=True)
        for n in tqdm(range(N + 1), desc=f"Write constraint {key}"):

            is_conblock_n = conblocks == n
            is_varblock_n = varblocks == n

            mask = is_conblock_n & is_equality
            filtered(arr[mask], is_varblock_0[mask], key).tofile(
                path / f"block{n}" / f"A_{suffix}", sep="\n"
            )
            mask = is_conblock_n & ~is_equality
            filtered(arr[mask], is_varblock_0[mask], key).tofile(
                path / f"block{n}" / f"C_{suffix}", sep="\n"
            )

            mask = is_conblock_L & is_equality
            filtered(arr[mask], is_varblock_n[mask], key).tofile(
                path / f"block{n}" / f"BL_{suffix}", sep="\n"
            )
            mask = is_conblock_L & ~is_equality
            filtered(arr[mask], is_varblock_n[mask], key).tofile(
                path / f"block{n}" / f"DL_{suffix}", sep="\n"
            )

            if n:
                mask = is_conblock_n & is_equality
                filtered(arr[mask], is_varblock_n[mask], key).tofile(
                    path / f"block{n}" / f"B_{suffix}", sep="\n"
                )
                mask = is_conblock_n & ~is_equality
                filtered(arr[mask], is_varblock_n[mask], key).tofile(
                    path / f"block{n}" / f"D_{suffix}", sep="\n"
                )


def non_bool_dict(d):
    """
    Convert bool to int for netCDF4 storing.
    """
    return {k: v if not isinstance(v, bool) else int(v) for k, v in d.items()}


def to_netcdf(m, *args, **kwargs):
    """
    Write out the model to a netcdf file.

    Parameters
    ----------
    m : linopy.Model
        Model to write out.
    *args
        Arguments passed to ``xarray.Dataset.to_netcdf``.
    **kwargs : TYPE
        Keyword arguments passed to ``xarray.Dataset.to_netcdf``.
    """

    def get_and_rename(m, attr, prefix=""):
        ds = getattr(m, attr)
        return ds.rename({v: prefix + attr + "-" + v for v in ds})

    vars = [
        get_and_rename(m.variables, attr, "variables_")
        for attr in m.variables.dataset_attrs
    ]
    cons = [
        get_and_rename(m.constraints, attr, "constraints_")
        for attr in m.constraints.dataset_attrs
    ]
    others = [get_and_rename(m, d) for d in m.dataset_attrs + ["objective"]]
    scalars = {k: getattr(m, k) for k in m.scalar_attrs}
    ds = xr.merge(vars + cons + others).assign_attrs(non_bool_dict(scalars))

    for k in ds:
        ds[k].attrs = non_bool_dict(ds[k].attrs)

    ds.to_netcdf(*args, **kwargs)


def read_netcdf(path, **kwargs):
    """
    Read in a model from a netcdf file.

    Parameters
    ----------
    path : path_like
        Path of the stored model.
    **kwargs
        Keyword arguments passed to ``xarray.load_dataset``.

    Returns
    -------
    m : linopy.Model
    """
    from linopy.model import Constraints, LinearExpression, Model, Variables

    m = Model()
    all_ds = xr.load_dataset(path, **kwargs)

    def get_and_rename(ds, attr, prefix=""):
        keys = [k for k in ds if k.startswith(prefix + attr + "-")]
        return ds[keys].rename({k: k[len(prefix + attr) + 1 :] for k in keys})

    attrs = Variables.dataset_attrs
    kwargs = {attr: get_and_rename(all_ds, attr, "variables_") for attr in attrs}
    m._variables = Variables(**kwargs, model=m)

    attrs = Constraints.dataset_attrs
    kwargs = {attr: get_and_rename(all_ds, attr, "constraints_") for attr in attrs}
    m._constraints = Constraints(**kwargs, model=m)

    for attr in m.dataset_attrs:
        setattr(m, attr, get_and_rename(all_ds, attr))
    m._objective = LinearExpression(get_and_rename(all_ds, "objective"))

    for k in m.scalar_attrs:
        setattr(m, k, all_ds.attrs.pop(k))

    return m
