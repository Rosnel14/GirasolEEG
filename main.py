# Importing the library

import serialParser



#threshold to say that user is concentrating
attn_Const = 50

#threshold to say user is meditating (eyes closed)
med_Const = 70

#threshold to say user
theta_Constant = 6000

#packet delay

delay = 5



def main():
    #testing each method

    #works - gets signal quality
    #print(serialParser.getSignalQuality(delay))

    # works - gets attention values
    print(serialParser.getAttention(delay))



#entry point for program
if __name__ == "__main__":
    main()
