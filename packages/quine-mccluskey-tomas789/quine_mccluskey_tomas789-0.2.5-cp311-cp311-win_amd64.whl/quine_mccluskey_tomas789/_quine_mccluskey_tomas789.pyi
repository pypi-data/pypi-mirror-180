"""quine_mccluskey_tomas789 C++ implementation"""
from __future__ import annotations
import _quine_mccluskey_tomas789
import typing

__all__ = [
    "ResultWithProfile",
    "combine_implicants",
    "complexity",
    "get_essential_implicants",
    "get_prime_implicants",
    "get_term_rank",
    "get_terms",
    "num2str",
    "permutations",
    "reduce_implicants",
    "reduce_simple_xnor_terms",
    "reduce_simple_xor_terms",
    "simplify",
    "simplify_los",
    "simplify_los_with_profile",
    "simplify_with_profile"
]


class ResultWithProfile():
    @property
    def profile_cmp(self) -> int:
        """
        :type: int
        """
    @property
    def profile_xnor(self) -> int:
        """
        :type: int
        """
    @property
    def profile_xor(self) -> int:
        """
        :type: int
        """
    @property
    def result(self) -> typing.Optional[typing.Set[str]]:
        """
        :type: typing.Optional[typing.Set[str]]
        """
    pass
def combine_implicants(a: str, b: str, dc: typing.Set[str]) -> typing.Optional[str]:
    pass
def complexity(implicant: str) -> float:
    pass
def get_essential_implicants(n_bits: int, terms: typing.Set[str], dc: typing.Set[str]) -> typing.Set[str]:
    pass
def get_prime_implicants(n_bits: int, use_xor: bool, terms: typing.Set[str]) -> ResultWithProfile:
    pass
def get_term_rank(term: str, term_range: int) -> int:
    pass
def get_terms(implicant: str) -> typing.Tuple[typing.List[int], typing.List[int], typing.List[int], typing.List[int], typing.List[int]]:
    pass
def num2str(n_bits: int, i: int) -> str:
    pass
def permutations(value: str, exclude: typing.Set[str]) -> typing.Set[str]:
    pass
def reduce_implicants(n_bits: int, implicants: typing.Set[str], dc: typing.Set[str]) -> typing.Set[str]:
    pass
def reduce_simple_xnor_terms(t1: str, t2: str) -> typing.Optional[str]:
    pass
def reduce_simple_xor_terms(t1: str, t2: str) -> typing.Optional[str]:
    pass
def simplify(ones: typing.List[int], dc: typing.List[int], num_bits: typing.Optional[int], use_xor: bool) -> typing.Optional[typing.Set[str]]:
    pass
def simplify_los(ones: typing.List[str], dc: typing.List[str], num_bits: typing.Optional[int], use_xor: bool) -> typing.Optional[typing.Set[str]]:
    pass
def simplify_los_with_profile(ones: typing.List[str], dc: typing.List[str], num_bits: typing.Optional[int], use_xor: bool) -> ResultWithProfile:
    pass
def simplify_with_profile(ones: typing.List[int], dc: typing.List[int], num_bits: typing.Optional[int], use_xor: bool) -> ResultWithProfile:
    pass
