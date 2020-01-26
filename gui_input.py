import tkinter as tk

class Windows(tk.Frame):
	def __init__(self, root):
		root.title("Patient Options")
		root.geometry("400x400")
		tk.Frame.__init__(self, root)
		b1 = tk.Button(self, text="Add patient", command = self.AddPatient)
		b1.pack(side="top", padx=40, pady=40)

	def AddPatient(self):
		self.window1 = tk.Toplevel(self)
		self.window1.title("Add Patient")
		self.window1.geometry("400x400")
		
		tk.Label(self.window1, text="Name").grid(row=0)
		tk.Label(self.window1, text="Age").grid(row=1)
		tk.Label(self.window1, text="Height (cm)").grid(row=2)
		tk.Label(self.window1, text="Weight (kg)").grid(row=3)

		self.Name = tk.Entry(self.window1)
		self.Age = tk.Entry(self.window1)
		self.Height = tk.Entry(self.window1)
		self.Weight = tk.Entry(self.window1)

		self.Name.grid(row=0, column=1)
		self.Age.grid(row=1, column=1) 
		self.Height.grid(row=2, column=1)
		self.Weight.grid(row=3, column=1)

		button1 = tk.Button(self.window1, text = "Enter", command = self.Confirm)
		button1.grid()
		
	def Confirm(self):
		self.vName = self.Name.get()
		self.vAge = self.Age.get()
		self.vHeight = self.Height.get()
		self.vWeight = self.Weight.get()
		
		self.window2 = tk.Toplevel(self)
		
		try:
			testAge = int(self.vAge)
			testHeight = int(self.vHeight)
			testWeight = int(self.vWeight)
			
			if self.vName:
				tk.Label(self.window2, text="Do you want to add this to the database?").grid(row=0, columnspan=2)
				button1 = tk.Button(self.window2, text = "Yes", command = self.EnterDetails)
				button2 = tk.Button(self.window2, text = "No", command = self.window2.destroy)
				button1.grid(row=1)
				button2.grid(row=1, column=1)
			else:
				label1 = tk.Label(self.window2, text="Please ensure the Name field is complete before submitting.")
				label1.pack()
				button1 = tk.Button(self.window2, text = "OK", command = self.window2.destroy)
				button1.pack()

		except ValueError:
			label1 = tk.Label(self.window2, text="Age, height and weight must be integers.")
			label1.pack()
			button1 = tk.Button(self.window2, text = "OK", command = self.window2.destroy)
			button1.pack()

	def EnterDetails(self):
		file = open('patients.txt','a')
		contents = '\n' + self.vName + ',' + self.vAge + ',' + self.vHeight + ',' + self.vWeight
		file.write(contents)
		file.close()
		self.window1.destroy()
		self.window2.destroy()

root = tk.Tk()
Windows(root).pack(side="top", fill="both", expand=True)
root.mainloop()