class men:
    name = "Anurag" 
    age = 25
    occupation = "Web developer"
    def display(self):
        print( f"{self.name} is a {self.occupation}" ) 
    

a = men() # class
a.display() # method


b = men()      #  another object of the same class
b.name = "Nitika" # modifying attribute of b's instance
b.occupation = "HR" # modifying attribute of b's instance
b.display() # calling b's method, it displays attributes of b not a's