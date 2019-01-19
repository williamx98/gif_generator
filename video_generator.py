from moviepy.editor import *
import sys

params = sys.argv
params_length = len(params)

if params_length < 5:
	print "Not enough arguments"
	sys.exit()

main_videofile = params[1]
pip_videofile = params[2]
musicfile = params[3]
title_text = params[4]
# demo_videofile = params[5]

pip = VideoFileClip(pip_videofile).resize(width=625)
pip = pip.set_pos(('left', 'bottom'))
pip = vfx.accel_decel(pip, 15)

main = VideoFileClip(main_videofile)

# main = main.speedx(factor=factor)
main = vfx.accel_decel(main, pip.duration)
main = main.set_pos(('center', 'center'))
main = main.resize(width=1920)

background = ColorClip(size=(1920, 1080), color=[0,0,0], duration=pip.duration)

music = AudioFileClip(musicfile)

title = TextClip(title_text, size=(1280, 1000), font="VerdanaB", color='white', stroke_color="black", stroke_width=7, method="caption", align="center")
title = title.set_pos(('center', 'center'))
title = title.set_duration(4)
title = title.resize(width=1080)

final_clip = CompositeVideoClip([background, main, pip, title])
final_clip = final_clip.set_audio(music)
final_clip = final_clip.set_duration(pip.duration)
final_clip = final_clip.resize(width=480)
final_clip.write_videofile("output.mp4")