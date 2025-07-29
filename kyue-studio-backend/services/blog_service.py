# is this where the schemas get sorted into different models / schemas ????



# load_content_from_s3() 



# for @blog_router.post("/create-post")
# async def create_post(
# 1) save markdown content 
# 2) save thumbnail 
# 3) create and save full combined metadata


# @blog_router.get("/posts", response_model=List[BlogPostMetadataSchema])
# async def get_all_blog_posts():
# 1. since this will be different in dynamodb, just lowkey put all of it into one function that returns all the posts


# @blog_router.get("/post/{post_id}", response_model=BlogPostMetadataSchema)
# async def get_post_metadata(post_id: uuid.UUID):
# 1. method to get the metadata (keep inside try catch block)

# @blog_router.delete("/post/{post_id}")
# async def delete_blog_post(post_id: uuid.UUID, token: str = Depends(oauth2_scheme)):
# 1. method to delete content markdown file (parameter is post_id)
# 2. method to delete thumbnail if it's not the default (parameter is post_id)
# 3. method to delete the metadata file  (parameter is post_id)
# keep the try catch block inside the endpoint method