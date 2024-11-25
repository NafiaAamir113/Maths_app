import streamlit as st
import sympy as sp

def parse_expression(expr):
    try:
        # Try to convert the expression to a symbolic expression
        sym_expr = sp.sympify(expr)
        return sym_expr
    except sp.SympifyError:
        # Return an error message if the input can't be parsed
        return "Invalid mathematical expression. Please check the syntax."

# Example usage:
expr = input("Enter your expression: ")
result = parse_expression(expr)
print(result)


# App title
st.title("Math Solver App: Linear Algebra, Integration, and Derivatives")

# Sidebar for user options
operation = st.sidebar.selectbox(
    "Select Operation",
    ["Linear Algebra", "Integration", "Derivatives"]
)

# Define the input fields
if operation == "Linear Algebra":
    st.header("Linear Algebra Solver")
    
    rows = st.number_input("Enter the number of rows for the matrix", min_value=1, max_value=10, value=2)
    cols = st.number_input("Enter the number of columns for the matrix", min_value=1, max_value=10, value=2)
    
    st.write("Enter the matrix elements:")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = st.number_input(f"Matrix[{i+1}][{j+1}]", key=f"mat_{i}_{j}")
            row.append(value)
        matrix.append(row)
        
    matrix = sp.Matrix(matrix)
    
    if st.button("Solve Linear Algebra"):
        st.write("Matrix:")
        st.write(matrix)
        st.write("Determinant:", matrix.det())
        if rows == cols:
            st.write("Inverse:")
            st.write(matrix.inv())
        else:
            st.write("Matrix is not square, inverse not possible.")

elif operation == "Integration":
    st.header("Integration Solver")
    
    expr = st.text_input("Enter the function to integrate (e.g., x**2 + sin(x))", "x**2")
    var = st.text_input("Enter the variable to integrate with respect to (e.g., x)", "x")
    
    if st.button("Solve Integration"):
        x = sp.Symbol(var)
        func = sp.sympify(expr)
        result = sp.integrate(func, x)
        st.write(f"The integral of {expr} with respect to {var} is:")
        st.latex(result)

elif operation == "Derivatives":
    st.header("Derivative Solver")
    
    expr = st.text_input("Enter the function to differentiate (e.g., x**3 + 3*x)", "x**3")
    var = st.text_input("Enter the variable to differentiate with respect to (e.g., x)", "x")
    
    if st.button("Solve Derivative"):
        x = sp.Symbol(var)
        func = sp.sympify(expr)
        result = sp.diff(func, x)
        st.write(f"The derivative of {expr} with respect to {var} is:")
        st.latex(result)

