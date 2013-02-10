#!/usr/bin/env/ python
# -*- coding: utf-8 -*-

__version__ = "0.9.2"
__description__ = "VMC-File-Parser for the C-Control II."

__copyright__ = """
   2-CB (C-Control-II kompatible Virtuelle Maschine).

  (C) 2007-2012 by Christoph Schueler <github.com/Christoph2,
                                       cpu12.gems@googlemail.com>

   All Rights Reserved

  This program is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 2 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License along
  with this program; if not, write to the Free Software Foundation, Inc.,
  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

from distutils.core import setup, Extension

def makeExtension(name):
        name = '_%s' % name.lower()
        nt = name[ 1 : ].title()

        swig_opts = [
                #'-c++',
                #'-features "autodoc"',
                '-MD',
                '-O',
                #'-modern',
                #'-modernargs',
                '-keyword'
        ]

        sources = [
                '%s.i' % nt,
                '../src/%s.c' % nt,
                '../src/Utl.c',
                'CommonMocks.c',
        ]

        include_dirs = ['../inc', '../hal']
        define_macros = [('SWIG', '1')]
        # define_macros : [(name : string, value : string|None)]
        # library_dirs : [string]
        # libraries : [string]
        # extra_compile_args : [string]
        # extra_link_args : [string

        return Extension(name = name, sources = sources, swig_opts = swig_opts,
            include_dirs = include_dirs, define_macros = define_macros
        )

setup(
  name = "vm2cb-tests",
  version = "0.1",
  author = "Christoph Schueler",
  description = "VM2CB Testsuite",
  ext_modules = [
      makeExtension('VM_Al'),
      makeExtension('VM_Cal'),
      makeExtension('VM_Can'),
      makeExtension('VM_Cntr'),
      makeExtension('VM_Com'),
      #makeExtension('Vm_Core'),
      makeExtension('VM_Hm'),
      makeExtension('VM_Iic'),
      makeExtension('VM_Lcd'),
      makeExtension('VM_Lpt'),
      makeExtension('VM_Ls'),
      makeExtension('VM_Math'),
      makeExtension('VM_Ports'),
      #makeExtension('VM_Tmr'),
      makeExtension('VM_Twb'),
      makeExtension('VM_Str'),
      makeExtension('VM_Plm'),
  ],
)

