============================
Django Algebraic Calculator
============================

Aplikasi web penghitungan aljabar untuk kelompok 7 Pemrograman Berbasis Penggunaan Ulang, Universitas Brawijaya.

==========
Anggota
==========

1.  205150400111052 - AURELIUS ALEXANDER VIRIYA
2.  205150407111019 - BAGAS RADITYA NUR LISTYAWAN
3.  205150407111025 - KHALIFFMAN RAHMAT HILAL
4.  205150407111016 - RIZAL AKBAR SYAH FAUZAN PUTRA

=====================
Installation & Usage
=====================

===============
Without UI
===============

1. Install on your project's virtual environment

2. Use this following syntax to install the package::

    'pip install -i https://test.pypi.org/simple/ algebra-collections==1.2'

3. Add 'algebra_calculator' to your Django project's "setting.py" INSTALLED_APPS::

    INSTALLED_APPS = [
        ...
        'algebra_calculator',
    ]

4. Import 'algebra_calculator' to your app's 'views.py' in order to use the pre-made Linear Equations or develop other type of Algebraic Equations

    Example using pre-made LinearEquations(linear.views file):

    from algebra_calculator import *

    def showXandYvalue():
    
        listOfChars = ['X', 'Y']
        listOfExpressions = ["2X + 5Y = 10", "3X + 2Y = 30"]

        result = LinearEquations.solve(2, listOfChars, listOfExpressions)

        for i in range(len(result)):
            printable(f"{listOfChars[i]}'s value is = {result}")

        return HttpResponse(printable)

    Example developing other type of Algebraic Equations (commutative.views file):


    class CommutativeAlgebra(AlgebraFactory):
        
        def solve(...):
        ...
        ...

    def finishCommutativeAlgebra():

        result = CommutativeAlgebra.solve(...)
        
        return HttpResponse(result)

===============
With UI
===============

1. Install on your project's virtual environment

2. Use this following syntax to install the package::

    'pip install -i https://test.pypi.org/simple/ algebra-collections==1.2'

3. Add 'algebra_calculator' and 'ui' to your Django project's "setting.py" INSTALLED_APPS::

        INSTALLED_APPS = [
        ...
        'algebra_calculator',
        'ui',
        ]

4. Include the poll URLconf in your project's urls.py::

    urlpattern = [
        ...
        path('[your_pathing_here/]', include('ui.urls')),
    ]

5. Access the Linear Equation's UI by running server and using the following url:

    127.0.0.1:8000/[your_pathing_here]/TwoExpression_LinearEquations