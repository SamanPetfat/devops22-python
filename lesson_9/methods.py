class square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return float(self.side **2)

    def circumference(self):
        return 4.0 * self.side

        #just made a new function with both inside, and made then float also. not sure if its a bad idea.
        # on the otherhand i wont need the singular "area" and "circumference". but ill save them for now.


    def area_and_circum(side1,side2):
        return float(side1 **2),float(side2 *4)
def main()

    area1= square.area_and_circum(side1=2,side2=2)

    area2= square.area_and_circum(side1=3.5, side2=3.5)

    print(
    
        f"First Area: {area1[0]} and circumference: {area1[1]}\n"
        f"Second Area: {area2[0]} and circumference: {area2[0]}"

        )
    
if __name__ == "__main__":
    main()
