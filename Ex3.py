class Fir():

    char1 = ' '
    char2 = '*'

    def print_fir(self, num):

        spaces = num-1
        needles = 1

        for i in range(num):
            print(
                (self.char1*spaces) +
                (self.char2*needles) +
                (self.char1*spaces)
            )
            needles += 2
            spaces -= 1


fir = Fir()
fir.print_fir(int(input()))
