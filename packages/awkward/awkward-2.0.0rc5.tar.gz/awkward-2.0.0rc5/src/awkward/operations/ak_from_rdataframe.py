# BSD 3-Clause License; see https://github.com/scikit-hep/awkward-1.0/blob/main/LICENSE

import awkward as ak


def from_rdataframe(rdf, columns):
    """
    Args:
        rdf (`ROOT.RDataFrame`): ROOT RDataFrame to convert into an
            Awkward Array.
        columns (str or tuple of str): A column or multiple columns to be
            converted to Awkward Array.

    Converts ROOT Data Frame columns into an Awkward Array.

    See also #ak.to_rdataframe.
    """
    with ak._errors.OperationErrorContext(
        "ak.from_rdataframe", dict(rdf=rdf, columns=columns)
    ):
        return _impl(rdf, columns)


def _impl(data_frame, columns):
    import awkward._connect.rdataframe.from_rdataframe  # noqa: F401

    return ak._connect.rdataframe.from_rdataframe.from_rdataframe(
        data_frame,
        columns,
    )
