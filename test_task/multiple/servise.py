class Multiple:

    def action(self, text):
        array=text.split()
        result=1
        for numer in array:
            result*=int(numer)
        return result
