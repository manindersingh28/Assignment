#1
from tkinter import *
def findGst():
    org_cost = int(org_priceField.get())
    N_price = int(net_priceField.get())
    gst_rate = ((N_price - org_cost) * 100) / org_cost;
    gst_rateField.insert(10, str(gst_rate) + " % ")

def clearAll():
    org_priceField.delete(0, END)
    net_priceField.delete(0, END)
    gst_rateField.delete(0, END)

if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="light green")
    gui.title("GST Rate Finder")
    gui.geometry("300x300")
    org_price = Label(gui, text="Original Price",
                      bg="blue")
    net_price = Label(gui, text="Net Price",
                      bg="blue")
    find = Button(gui, text="Find", fg="Black",
                  bg="Red",
                  command=findGst)
    gst_rate = Label(gui, text="Gst Rate", bg="blue")
    clear = Button(gui, text="Clear", fg="Black",
                   bg="Red",
                   command=clearAll)
    org_price.grid(row=1, column=1, padx=10, pady=10)

    net_price.grid(row=2, column=1, padx=10, pady=10)

    find.grid(row=3, column=2, padx=10, pady=10)

    gst_rate.grid(row=4, column=1, padx=10, pady=10)

    clear.grid(row=5, column=2, padx=10, pady=10)

    org_priceField = Entry(gui)

    net_priceField = Entry(gui)

    gst_rateField = Entry(gui)

    org_priceField.grid(row=1, column=2, padx=10, pady=10)

    net_priceField.grid(row=2, column=2, padx=10, pady=10)

    gst_rateField.grid(row=4, column=2, padx=10, pady=10)

    gui.mainloop()

#2
from tkinter import *

import calendar

def showCal():
    new_gui = Tk()
    new_gui.config(background="white")
    new_gui.title("CALENDAR")
    new_gui.geometry("550x600")

    fetch_year = int(year_field.get())
    cal_content = calendar.calendar(fetch_year)
    cal_year = Label(new_gui, text=cal_content, font="Consolas 10 bold")
    cal_year.grid(row=5, column=1, padx=20)
    new_gui.mainloop()

if __name__ == "__main__":
    gui = Tk()
    gui.config(background="white")
    gui.title("CALENDAR")
    gui.geometry("250x140")
    cal = Label(gui, text="CALENDAR", bg="dark gray",
                font=("times", 28, 'bold'))

    year = Label(gui, text="Enter Year", bg="light green")
    year_field = Entry(gui)
    Show = Button(gui, text="Show Calendar", fg="Black",
                  bg="Red", command=showCal)
    Exit = Button(gui, text="Exit", fg="Black", bg="Red", command=exit)
    cal.grid(row=1, column=1)

    year.grid(row=2, column=1)

    year_field.grid(row=3, column=1)

    Show.grid(row=4, column=1)

    Exit.grid(row=6, column=1)
    gui.mainloop()

#3
from tkinter import *
expression = ""

def press(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)

def equalpress():
	try:

		global expression

		total = str(eval(expression))
		equation.set(total)
		expression = ""

	except:

		equation.set(" error ")
		expression = ""

def clear():
	global expression
	expression = ""
	equation.set("")

if __name__ == "__main__":
	gui = Tk()
	gui.configure(background="light green")
	gui.title("Simple Calculator")
	gui.geometry("270x150")
	equation = StringVar()
	expression_field = Entry(gui, textvariable=equation)
	expression_field.grid(columnspan=4, ipadx=70)
	button1 = Button(gui, text=' 1 ', fg='black', bg='red',
					command=lambda: press(1), height=1, width=7)
	button1.grid(row=2, column=0)

	button2 = Button(gui, text=' 2 ', fg='black', bg='red',
					command=lambda: press(2), height=1, width=7)
	button2.grid(row=2, column=1)

	button3 = Button(gui, text=' 3 ', fg='black', bg='red',
					command=lambda: press(3), height=1, width=7)
	button3.grid(row=2, column=2)

	button4 = Button(gui, text=' 4 ', fg='black', bg='red',
					command=lambda: press(4), height=1, width=7)
	button4.grid(row=3, column=0)

	button5 = Button(gui, text=' 5 ', fg='black', bg='red',
					command=lambda: press(5), height=1, width=7)
	button5.grid(row=3, column=1)

	button6 = Button(gui, text=' 6 ', fg='black', bg='red',
					command=lambda: press(6), height=1, width=7)
	button6.grid(row=3, column=2)

	button7 = Button(gui, text=' 7 ', fg='black', bg='red',
					command=lambda: press(7), height=1, width=7)
	button7.grid(row=4, column=0)

	button8 = Button(gui, text=' 8 ', fg='black', bg='red',
					command=lambda: press(8), height=1, width=7)
	button8.grid(row=4, column=1)

	button9 = Button(gui, text=' 9 ', fg='black', bg='red',
					command=lambda: press(9), height=1, width=7)
	button9.grid(row=4, column=2)

	button0 = Button(gui, text=' 0 ', fg='black', bg='red',
					command=lambda: press(0), height=1, width=7)
	button0.grid(row=5, column=0)

	plus = Button(gui, text=' + ', fg='black', bg='red',
				command=lambda: press("+"), height=1, width=7)
	plus.grid(row=2, column=3)

	minus = Button(gui, text=' - ', fg='black', bg='red',
				command=lambda: press("-"), height=1, width=7)
	minus.grid(row=3, column=3)

	multiply = Button(gui, text=' * ', fg='black', bg='red',
					command=lambda: press("*"), height=1, width=7)
	multiply.grid(row=4, column=3)

	divide = Button(gui, text=' / ', fg='black', bg='red',
					command=lambda: press("/"), height=1, width=7)
	divide.grid(row=5, column=3)

	equal = Button(gui, text=' = ', fg='black', bg='red',
				command=equalpress, height=1, width=7)
	equal.grid(row=5, column=2)

	clear = Button(gui, text='Clear', fg='black', bg='red',
				command=clear, height=1, width=7)
	clear.grid(row=5, column='1')

	Decimal= Button(gui, text='.', fg='black', bg='red',
					command=lambda: press('.'), height=1, width=7)
	Decimal.grid(row=6, column=0)

	gui.mainloop()

#4

def merge(arr, l, m, r):
	n1 = m - l + 1
	n2 = r - m

	L = [0] * (n1)
	R = [0] * (n2)

	for i in range(0, n1):
		L[i] = arr[l + i]

	for j in range(0, n2):
		R[j] = arr[m + 1 + j]

	i = 0
	j = 0
	k = l

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1

def mergeSort(arr, l, r):
	if l < r:

		m = l+(r-l)//2

		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)

arr = eval(input("Enter the marks of students :"))
n = len(arr)
print("Given array is")
for i in range(n):
	print("%d" % arr[i],end=" ")

mergeSort(arr, 0, n-1)
print("\n\nSorted array is")
for i in range(n):
	print("%d" % arr[i],end=" ")

#5

def merge(lst, l, m, r):
	n1 = m - l + 1
	n2 = r - m

	L = [0] * (n1)
	R = [0] * (n2)

	for i in range(0, n1):
		L[i] = lst[l + i]

	for j in range(0, n2):
		R[j] = lst[m + 1 + j]

	i = 0
	j = 0
	k = l

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			lst[k] = L[i]
			i += 1
		else:
			lst[k] = R[j]
			j += 1
		k += 1

	while i < n1:
		lst[k] = L[i]
		i += 1
		k += 1

	while j < n2:
		lst[k] = R[j]
		j += 1
		k += 1

def mergeSort(lst, l, r):
	if l < r:

		m = l+(r-l)//2

		mergeSort(lst, l, m)
		mergeSort(lst, m+1, r)
		merge(lst, l, m, r)

def binary_search(lst, x):
	low = 0
	high = len(lst) - 1
	mid = 0

	while low <= high:

		mid = (high + low) // 2

		if lst[mid] < x:
			low = mid + 1
		elif lst[mid] > x:
			high = mid - 1

		else:
			return mid

	return -1

lst=eval(input("Enter a list with duplicates numbers"))
n = len(lst)
print("Given array is")
for i in range(n):
	print("%d" % lst[i],end=" ")

mergeSort(lst, 0, n-1)
print("\n\nSorted array is")
for i in range(n):
	print("%d" % lst[i],end=" ")

x = int(input("\nEnter the element to search :"))
result = binary_search(lst,x)

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")
print("The number of occurence of",x,"is",lst.count(x))

#6
def remove(dupli):
	final_list = []
	for num in dupli:
		if num not in final_list:
			final_list.append(num)
	return final_list

def bubbleSort(rlst):
	n = len(rlst)
	for i in range(n):
		for j in range(0, n-i-1):
			if dupli[j] > dupli[j+1]:
				rlst[j], rlst[j+1] = rlst[j+1], rlst[j]

dupli =eval(input("Enter a list with duplicate numbers"))
rlst=remove(dupli)
print(rlst)

bubbleSort(rlst)

print("Sorted array is:")
for i in range(len(rlst)):
    print("%d" % rlst[i], end=" ")



