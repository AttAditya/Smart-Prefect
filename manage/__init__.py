import manage.server as server
import manage.info as info
import manage.fun as fun
import manage.music as music
import manage.knowledge as knowledge

command_data = {}
command_data.update(server.index)
command_data.update(fun.index)
command_data.update(info.index)
command_data.update(music.index)
command_data.update(knowledge.index)

