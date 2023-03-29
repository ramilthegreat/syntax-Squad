    self.my_label = tk.Label(master, text="Grading Calculator")
    self.my_label.grid(row=1, column=1)

    
    self.A_label = tk.Label(master, text="First sub:")
    self.A_label.grid(row=3, column=0)

    self.A_input = tk.Entry(master)
    self.A_input.grid(row=3, column=1)

    self.B_label = tk.Label(master, text="second sub:")
    self.B_label.grid(row=4, column=0)

    self.B_input = tk.Entry(master)
    self.B_input.grid(row=4, column=1)

    self.C_label = tk.Label(master, text="third sub:")
    self.C_label.grid(row=5, column=0)

    self.C_input = tk.Entry(master)
    self.C_input.grid(row=5, column=1)

    self.D_label = tk.Label(master, text="fourth sub:")
    self.D_label.grid(row=6, column=0)
    
    self.D_input = tk.Entry(master)
    self.D_input.grid(row=6, column=1)

    
    self.calculate_button = tk.Button(master, text="Calculate Grade", command=self.calculate_grade)
    self.calculate_button.grid(row=7, column=1)

    
    self.total_label = tk.Label(master,text="")
    self.total_label.grid(row =8, column =1)
    
    self.percentage_label =tk.Label(master,text="")
    self.percentage_label.grid(row = 9,column=1)
    
    self.grade_label = tk.Label(master, text="")
    self.grade_label.grid(row=11, column=1)
    
    self.number =tk.Label(master,text="")
    self.number.grid(row =2, column =1)

def calculate_grade(self):
    try:
        
    
     A = float(self.A_input.get())
     B = float(self.B_input.get())
     C = float(self.C_input.get())
     D = float(self.D_input.get())
     
     
     overall_grade = A + B + C + D
     percentage = (overall_grade /400)*100
    
    
     if percentage >= 90:
         letter_grade = "excellent"
     elif percentage >= 85:
         letter_grade = "Very good"
     elif percentage >= 80:
         letter_grade = "Good!"
     elif percentage >= 75:
         letter_grade = "Still pass"
     else:
         letter_grade = "Fail!"

    
     self.total_label.config(text="your total grade =%.2f" % overall_grade)
     
     self.percentage_label.config(text="Your grade percentage =%.2f"%percentage)
     
     self.grade_label.config(text="Your grade is: " + letter_grade)
           
    except ValueError:
           self.number.config(text="Please enter a number")