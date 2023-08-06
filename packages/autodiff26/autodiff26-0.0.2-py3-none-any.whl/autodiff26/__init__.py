#!/usr/bin/env python3
# File       : __init__.py
# Description: Initialize package
# Copyright 2022 Harvard University. All Rights Reserved.

r"""Packages For Forward and Reverse Mode Automatic Differentiation"""
from .forward_mode.ad_calculator import autodiff, ad
from .reverse_mode.reverse_calculator import reversediff, rev_ad

__all__ = ['ad', 'autodiff','rev_ad', 'reversediff']




