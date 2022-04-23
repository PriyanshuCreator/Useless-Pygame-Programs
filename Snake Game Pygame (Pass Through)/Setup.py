import cx_Freeze
executables = [cx_Freeze.Executable("Snake Game.py")]
cx_Freeze.setup(
    name = "Generic Snake Game",
    options = {"build_exe":{"packages":["pygame"],"include_files":["Snake_head.png","music.mp3",'icon.png','apple.png','background.jpg']}}
    , description = "This is Just a Normal Snake Game",
    executables = executables
)