class Blog
    """Blog class for storing listing of blog entries
    """
    def __init__(self) -> None:
        """Creates Blog object and sets initial values for metadata
        """
        _entry_list = list()
        metadata = {"title":"my_blog", "subtitle":"my_subtitle" }

    def get_entry(all: bool) -> BlogEntry | list(BlogEntry):
        """Gets blog entry. If all is true, returns entire BlogEntry list

        Args:
            all (bool): Switch to return all BlogEntry values

        Returns:
            BlogEntry: Blog entry object 
        """
        pass

    def add_entry(entry: BlogEntry) -> None:
        """Appends BlogEntry to end of blog list

        Args:
            entry (BlogEntry): BlogEntry to be appended to Blog
        """
        pass

    def update_entry(this_entry: BlogEntry, new_entry: BlogEntry) -> int | None: 
        """Update this_entry BlogEntry list with new_entry BlogEntry 

        Args:
            entry (BlogEntry): _description_
        
        Returns: 
            BlogEntry: reference to 
        """
        pass