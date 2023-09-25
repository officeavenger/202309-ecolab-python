import help
import utils.commons



def main():
    print(type(help))
    print(type(utils))
    print(dir(utils))
    print(type(utils.commons))
    print(utils.commons.members(help))
    
    
    help.about()
    print(help.version)

main()