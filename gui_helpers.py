""" GUI Helper Functions """

def forget_all_frames(parent, current):
    for widget in parent.winfo_children():
        if  widget != current:
            widget.pack_forget()   # or widget.grid_forget(), widget.place_forget()

def show_merge_frame(merge_frame, root):
    merge_frame.pack(fill='both', expand=True)
    root.title("Magic PDF - Merge")
    forget_all_frames(root, merge_frame)

def show_compress_frame(compress_frame, root):
    compress_frame.pack(fill='both', expand=True)
    root.title("Magic PDF - Compress")
    forget_all_frames(root, compress_frame)

def show_rotate_frame(rotate_frame, root):
    rotate_frame.pack(fill='both', expand=True)
    root.title("Magic PDF - Rotate")
    forget_all_frames(root, rotate_frame)

def show_split_frame(split_frame, root):
    split_frame.pack(fill='both', expand=True)
    root.title("Magic PDF - Split")
    forget_all_frames(root, split_frame)