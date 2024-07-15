import datetime
class BlogMetadata:
    """Data structure for storing metadata needed for blog and entries.
    """
    def __init__(self, title: str = "", 
                subtitle: str = "", 
                author: str = "", 
                time_created: datetime = datetime.datetime.now(),
                time_updated: datetime = datetime.datetime.now(),
                id: str = "") -> None:
        """Creates new BlogMetadata object. Defaults to blank values.

        Args:
            title (str, optional): Title of item. Defaults to "".
            subtitle (str, optional): Subtitle or description. Defaults to "".
            author (str, optional): author name to be displayed. Defaults to "".
            time_created (datetime, optional): Initial create datetime. Defaults to datetime.datetime.now().
            time_updated (datetime, optional): Last updated datetime. Defaults to datetime.datetime.now().
            id (str, optional): Unique ID of object. Defaults to "".
        """
        metadata = {
            "title":title, 
            "subtitle":subtitle, 
            "author":author, 
            "time_created":time_created,
            "time_updated":time_updated,
            "id":id
            }
        pass

class BlogEntry:
    """BlogEntry object for Blog content
    """

    def __init__(self, entry_metadata: BlogMetadata = BlogMetadata(), 
                 entry_text: str = "", 
                 entry_blurb: str = "") -> None:
        """Creates BlogEntry, defaults to blank values

        Args:
            entry_metadata (BlogMetadata, optional): BlogEntry identifying metadata. Defaults to BlogMetadata().
            entry_text (str, optional): Content text of entry. Defaults to "".
            entry_blurb (str, optional): Short blurb description of entry. Defaults to "".
        """
        metadata = entry_metadata
        text = entry_text
        blurb = entry_blurb
        pass

class Blog:
    """Blog class for storing listing of blog entries
    """
    def __init__(self) -> None:
        """Creates Blog object and sets blank initial values for metadata
        """
        _entry_list = list(BlogEntry())
        metadata = BlogMetadata()

    def get_entry(self, all: bool) -> BlogEntry | list(BlogEntry):
        """Gets blog entry. If all is true, returns entire BlogEntry list

        Args:
            all (bool): Switch to return all BlogEntry values

        Returns:
            BlogEntry: Blog entry object 
        """
        pass

    def add_entry(self, entry: BlogEntry) -> None:
        """Appends BlogEntry to end of blog list

        Args:
            entry (BlogEntry): BlogEntry to be appended to Blog
        """
        pass

    def update_entry(self, this_entry: BlogEntry, new_entry: BlogEntry) -> bool: 
        """Update this_entry in BlogEntry list with new_entry BlogEntry object 

        Args:
            entry (BlogEntry): _description_

        Returns:
        bool: True if successfully updated, otherwise false
        """
        pass

    def delete_entry(self, entry: BlogEntry) -> bool:
        """Deletes given BlogEntry from blog list

        Args:
            entry (BlogEntry): BlogEntry to be deleted

        Returns:
            bool: True if successfully deleted, otherwise false
        """
        pass
