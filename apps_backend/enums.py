# used for classifying the distinctions in app 


from enum import Enum

class CategoryType(Enum) :
    ALBUMS = "albums"
    VIDEOS = "videos"
    TRACKS = "tracks"

class VideoType(Enum) :
    TRAILERS = "trailers"
    TOP_VIDEOS = "top_videos"
    GUPSHUPS = "gupshups"
    EVERGREEN = "evergreen"
    TRACKS = "tracks"

class Type(Enum) :
    ALBUM = "album"
    VIDEO = "video"
    TRACK = "track"
