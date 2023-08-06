import sys
import logging

import defopt

from pathlib import Path

import primaschema.lib as lib


logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)


def hash_bed(bed_path: Path):
    """
    Generate a bed file checksum

    :arg ref_path: Path of bed file
    """
    hex_digest = lib.hash_bed(bed_path)
    print("BED checksum:", file=sys.stderr)
    print(hex_digest)


def hash_ref(ref_path: Path):
    """
    Generate reference sequence checksum

    :arg ref_path: Path of reference sequence
    """
    hex_digest = lib.hash_ref(ref_path)
    print("Reference checksum:", file=sys.stderr)
    print(hex_digest)


def validate(scheme_dir: Path):
    """
    Validate a primer scheme bundle containing info.yaml, primer.bed and reference.fasta

    :arg scheme_dir: Path of scheme.bed file
    :arg out_dir: Path of directory in which to save primer.bed
    :arg force: Overwrite existing output files
    """
    return lib.validate(scheme_dir)


def build(scheme_dir: Path, out_dir: Path = Path(), force: bool = False):
    """
    Build a primer scheme bundle containing info.yaml, primer.bed and reference.fasta

    :arg scheme_dir: Path of scheme.bed file
    :arg out_dir: Path of directory in which to save primer.bed
    :arg force: Overwrite existing output files
    """
    lib.build(scheme_dir=scheme_dir, out_dir=out_dir, force=force)


def six_to_seven(
    bed_path: Path, fasta_path: Path, out_dir: Path = Path(), force: bool = False
):
    """
    Convert a 6 column scheme.bed file to a 7 column primer.bed file using a reference sequence

    :arg bed_path: Path of scheme.bed file
    :arg fasta_path: Path of reference sequence
    :arg out_dir: Path of directory in which to save primer.bed
    :arg force: Overwrite existing output files
    """
    lib.convert_scheme_bed_to_primer_bed(
        bed_path=bed_path, fasta_path=fasta_path, out_dir=out_dir, force=force
    )


def build_recursively(root_dir: Path, force: bool = False):
    """
    Recursively build a primer scheme bundles in the provided directory

    :arg root_dir: Path of scheme.bed file
    :arg force: Overwrite existing schemes and ignore hash check failures
    """
    lib.build_recursively(root_dir=root_dir, force=force)


def main():
    defopt.run(
        {
            "hash-ref": hash_ref,
            "hash-bed": hash_bed,
            "validate": validate,
            "build": build,
            "build-recursively": build_recursively,
            "6to7": six_to_seven,
        },
        no_negated_flags=True,
        strict_kwonly=False,
        short={},
    )


if __name__ == "__main__":
    main()
