def main():
    extension = input("Filename: ").strip().lower().split(".")[-1]
    
    match extension:
        case 'gif' | 'png' | 'jpg' | 'jpeg':
            print(f"image/{extension}")
        case 'pdf' | 'zip':
            print(f"application/{extension}")
        case 'txt':
            print("text/plain")
        case _:
            print("application/octet-stream")

main()