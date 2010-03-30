======================================================
Python
======================================================

What is Python?
---------------

Python is a modern, multi-paradigm, programming language that is increasingly used for scientific computation.

Python was a language designed to be both easy to teach and industrial-strength. It is one of the most widely used languages in the world for general purpose programming. Over the last few years, scientific libraries in Python have matured to a point where they make the language a strong candidate for science.

The numpy library is a *de facto* standard numerical array library, while the scipy collection of libraries provide access to basic scientific tools (e.g., statistical toolbox, linear algebra), often by providing access to mature code written in other languages. In fact, Python is a very good glue language: you can easily access code written in Fortran, C, or C++ directly from Python.

The python interpreter is open-source as are most of the basic libraries that support scientific computing. This means that it can be used on any platform, by anyone, anywhere.

Why not Matlab?
---------------

Matlab is a good solution for data exploration or small computations. If you are using its command-line directly, it is very convenient. In fact, many of the tools covered in this class are inspired (or, at the very least, influenced by Matlab).

However, the moment you save commands to a file, I would argue you are writing software (even if on a small scale). For this, Matlab is less appropriate. In part, the same characteristics that make it a convenient tool at the command-line, make it unusable for even small scale software projects. The flat namespace or the fact that each function corresponds to a file are two characteristics that aid command-line use, but hinder software writing. In this sense, it is similar to a Unix shell: fast to use if you're typing commands directly, but not scalable.

Matlab is still, at its core, a matrix processing language. For matrix processing, its expressive power is unmatched, at the cost of forcing everything else to conform to it. String processing is especially painful. Therefore, I rather choose a language that can be used in any domain.
