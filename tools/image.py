class Image():
    def __init__(self, image_args)->None:
        self.activity = image_args.activity
        self.product = image_args.product
        self.tag = image_args.tag_name
        self.chop = image_args.chop