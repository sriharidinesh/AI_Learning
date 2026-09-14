class Call():
    def subfields():
        lists = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural language Processing"]
        print("Sub-fields in AI are:")
        for i in lists:
            print(i)
    def OddEven():
        num = int(input("Enter the Number:"))
        if ((num %2) == 0):
            print(f"{num} is Even Number")
        else:
            print(f"{num} is Odd Number")
    def Eligible():
        print("To Check Eligiblity For Marriage.")
        gender = input("Press 'M' for male (or) Press 'F' for Female").upper()
        age = int(input("Enter the Age: "))
        if gender == 'M':
            if age >=21:
                print(f"Your Gender:Male\nYour Age:{age}\nEligible")
            else:
                print(f"Your Gender:Male\nYour Age:{age}\nNot Eligible")
        else:
            if age >=18:
                print(f"Your Gender:Female\nYour Age:{age}\nEligible")
            else:
                print(f"Your Gender:Female\nYour Age:{age}\nNot Eligible")
    def Percentage():
        lists = [98,87,95,95,93]
        total = 0
        j = 1
        for i in lists:
            print(f"Subject{j}= {i}")
            total += i
            j += 1
        percent = float(total/5)
        print(f"Total : {total}\nPercentage : {percent}")
    def AreaOfTriangle():
        print("To check the Area of the traingle.")
        height = int(input("Enter the Height: "))
        breadth = int(input("Enter the Breadth: "))
        area = float((height*breadth)/2)
        print(f"Height: {height}\nBreadth: {breadth}\nArea Formula: (Height*Breadth)/2\nArea Of The Triangle: {area}")
    def PerimeterOfTriangle():
        print("To check the Perimeter of the traingle.")
        height1 = int(input("Enter the Height1: "))
        height2 = int(input("Enter the Height2: "))
        breadth = int(input("Enter the Breadth: "))
        perimeter = height1+height2+breadth
        print(f"Height1: {height1}\nHeight2: {height2}\nBreadth: {breadth}\nPermieter Formula: Height1+Height2+Breadth\nPerimeter Of The Triangle: {perimeter}")
    