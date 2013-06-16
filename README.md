pycppreflect 
=============

A set of python scripts to handle cpp reflection using Clang as a
preprocessor step.

So why write a wrapper for Clang's existing wrapper?
----------------------------------------------------

Fair question.  :)  Clang already provides a complete set
of python bindings for libclang that work very well.  

What I wanted was a way to flatten Clang's syntax tree.
Not seeing such a method, I started writing one.  Part
way through that task I realized that all I really needed
was the string syntax, not all the extra parsing kruft.

So I started adding little helper snippets here and there,
resulting in pycppreflect.  

Installation
------------

1. Download llvm.  Use my [mirror](https://github.com/Jerdak/llvm-mirror)
2. Download clang.  Use my [mirror](https://github.com/Jerdak/clang-mirror)
3. Follow clang installation instructions but use my mirrored versions instead*
4. Install clang python bindings, located in llvm/tools/clang/bindings/python.** ( See [instructions](http://eli.thegreenplace.net/2011/07/03/parsing-c-in-python-with-clang/) )
5. Try out the examples.  example_extern.py is a good start

*: It isn't necessary to use my versions, just be aware that there is a [slight
glitch](http://www.seethroughskin.com/blog/?p=2172)  

**: If you use the original clang python bindings, by aware that there isn't a 
`Cursor.get_argument_list` method in the original.  

Todo
-----
- [ ] Port all additional pycppreflect code from local repo
- [ ] Add additional cursor handlers
- [x] Add example filters like UnityDllImport.py
- [ ] Add code to limit the reach of the flattened output
- [ ] Clean .py code a bit to remove redundant data
- [ ] Replace TypeKind values with canonical CPP types
