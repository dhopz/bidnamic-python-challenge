# Import the transform script
#from scripts import extract, transform
import transform
import extract
from insights import insight_all


# Call its main function
if __name__ == "__main__":
    extract.main()
    transform.main()  
    insight_all.main()
    print("[Pipeline] Complete")