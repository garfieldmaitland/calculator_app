# Install necessary libraries
!pip install gradio

# Import necessary libraries
import gradio as gr

# Create the calculator class
def calculator(num1, operation, num2):
  if operation == "add":
    return num1 + num2
  elif operation == "subtract":
    return num1 - num2
  elif operation == "multiply":
    return num1 * num2
  elif operation == "exponentiate":
    return num1 ** num2
  elif operation == "divide":
    if num2 == 0:
      raise gr.Error("Cannot divide by zero!")
    return num1 / num2

calculator_app = gr.Interface(
  calculator,
  [
    "number",
    gr.Radio(["add", "subtract", "multiply", "exponentiate", "divide"]),
    "number"
  ],
  "number",
  examples=[
    [1, "add", 1],
    [30, "subtract", 20],
    [100, "divide", 5],
    [7, "multiply", 10],
    [2, "exponentiate", 3],
  ],
  title="Calculator Application",
  description="This is a sample calculator application.",
  css="footer {display:none !important}:
)

calculator_app.launch()
