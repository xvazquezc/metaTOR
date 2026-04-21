# Unit tests for host interacting-contig threshold helpers.

import pytest

import metator.host as mth


def test_get_required_interacting_contigs_without_proportion():
    assert mth.get_required_interacting_contigs(10, 5, None) == 5


def test_get_required_interacting_contigs_with_proportion_rounds_up():
    assert mth.get_required_interacting_contigs(1, 5, 0.1) == 1
    assert mth.get_required_interacting_contigs(9, 5, 0.1) == 1
    assert mth.get_required_interacting_contigs(10, 5, 0.1) == 1
    assert mth.get_required_interacting_contigs(11, 5, 0.1) == 2


def test_get_required_interacting_contigs_with_one_proportion():
    assert mth.get_required_interacting_contigs(7, 5, 1.0) == 7


def test_get_required_interacting_contigs_with_zero_contigs_stays_positive():
    assert mth.get_required_interacting_contigs(0, 5, 0.1) == 1


def test_get_required_interacting_contigs_invalid_proportion_low():
    with pytest.raises(ValueError):
        mth.get_required_interacting_contigs(10, 5, 0)


def test_get_required_interacting_contigs_invalid_proportion_high():
    with pytest.raises(ValueError):
        mth.get_required_interacting_contigs(10, 5, 1.1)
