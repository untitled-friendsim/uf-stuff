default:
	cd fansim-engine && git pull
	rm -rf fansim-engine/custom_volumes/*
	rm -rf fansim-engine/skins/untitled-friendsim
	cp -r custom_volumes/* fansim-engine/custom_volumes
	cp -r skins/* fansim-engine/skins
	cd fansim-engine/src && python3 run_wizard.py --verbose --clean --skins untitled-friendsim

clean:
	rm -rf fansim-engine/
	git clone https://github.com/giovanh/fansim-engine

renpy:
	../renpy-7.4.6-sdk/renpy.sh
