===============
Projects
===============

There are two possibilities: self-proposed or class project. A part of the teaching goals of the class is to teach you tools and techniques for medium-scale collaboration. Therefore, the class project is done by all interested students. Each student (or small group) will work on a separate bit of the project (on which they will be evaluated), but they must make sure that their piece of code *plays well with others*.

Class Project
--------------

The class project is to be done by all students, but will be broken up into individual chunks.

The overall goal of the project is to (1) simulate a video of particles moving in space, (2) from the video *track the particles*, (3) compare the results of tracking with the simulated tracks. This is to be broken into several pieces, each of which is assigned to one or two students (in brackets, the names of the students working on it):

    1. Object position generator
    2. Image generator
    3. Object detection [Peng Liu]
    4. Object tracking [Andrej Savol]
    5. Results visualisation
    6. Statistics collector [Longzhu Shen]

We will also spend some class time going over the structure and design of the program.

To participate in the project, please 

    1. Get a google account (you can use any email)
    2. Email me the email you used to get a google account
    3. Wait for me to add you to the project (I'll reply to your email when I've done so)
    4. Go to the `particles webpage`_ and follow the instructions to downloading the code from google's subversion. You need to be logged in to google to have *write access* to the subversion repository.
    5. Add your name to the AUTHORS.txt file and commit

.. _`particles webpage`: http://code.google.com/p/particles/

Self-Proposed
---------------

If you want to propose a project, you can as long as you fulfill most of the following conditions:

    1. It must be self-contained and be at least 300 lines of code (not counting tests &c).
    2. It must be done in Python.
    3. It should use numpy.
    4. It should include tests and documentation.
    5. It should use version control.
    6. It should either be a part of a bigger project or involve working with libraries/modules not presented in the course (and not written by you).

