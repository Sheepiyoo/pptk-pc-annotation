if __name__ == "__main__":
    import pickle
    import argparse
    import os
    import pptk
    import numpy as np
    import time

    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    
    print("Loading ", args.filename)

    name = os.path.splitext(os.path.basename(args.filename))[0]
    np_pcd = np.load(args.filename)

    # Invert y values for visualisation
    np_single = np_pcd[:, :3] * np.tile([1,-1,1], (np_pcd.shape[0], 1))
    labels = np_pcd[:,3]

    print("Before: ", np_pcd[:10])
    v = pptk.viewer(np_single, labels)

    while True:
        try:
            v.wait()
            selected = v.get('selected')
            
            print(len(selected))
            if len(selected) == 0: 
                break

            label_id = int(input("Enter new class label (0 for non-traversable, 1 for traversable): "))
            labels[selected] = label_id

            v.clear()
            v.load(np_single, labels)
        
        except KeyboardInterrupt:
            print("Labelling complete")
            break

    print("After: ", np_pcd[:10])

    v.close()
    
    np.save(args.filename, np_pcd)