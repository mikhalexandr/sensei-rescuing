import pygame
import webbrowser
from config import consts
import menu
from items.static.stars import Object, Button
from managing.items_managing import fullscreenChanger, volumeChanger
from misc.utils import terminate, transition


def settings_menu():
    title = Object(windows.width // 2 - 743 / 2 if consts.languageNow == 'rus' else windows.width // 2 - 671 / 2,
                   windows.height // 2 - 534 // 2,
                   656 if consts.languageNow == 'rus' else 584, 82,
                   fr"objects\{consts.languageNow}\settings-title-obj.png")
    cross_btn = Button(title.x + title.width + 20, title.y + 8, 67, 72, r"buttons\without text\default-cross-btn.png",
                       r"buttons\without text\hover-cross-btn.png",
                       r"buttons\without text\press-cross-btn.png", r"data\sounds\menu-button-sound.mp3")

    field_audio = Object(windows.width // 2 - 435, title.y + 104, 420, 430,
                         fr"objects\{consts.languageNow}\audio-field-obj.png")
    music_name = Object(field_audio.x + field_audio.width / 2 - 385 / 2,
                        title.y + 238, 385, 34, fr"objects\{consts.languageNow}\music-obj.png")
    sound_name = Object(field_audio.x + field_audio.width / 2 - 380 / 2, title.y + 372,
                        380, 34, fr"objects\{consts.languageNow}\sound-obj.png")
    music_slider_obj = Object(field_audio.x + field_audio.width / 2 - 302 / 2, music_name.y + music_name.height + 26,
                              302, 16,
                              r"objects\without text\slider-obj.png")
    sound_slider_obj = Object(field_audio.x + field_audio.width / 2 - 302 / 2, sound_name.y + sound_name.height + 26,
                              302, 16,
                              r"objects\without text\slider-obj.png")
    music_slider_btn = Button(music_slider_obj.x + music_slider_obj.width * consts.wM,
                              music_slider_obj.y + music_slider_obj.height / 2 - 14, 26, 28,
                              r"buttons\without text\default-slider-btn.png",
                              r"buttons\without text\hover-slider-btn.png",
                              r"buttons\without text\press-slider-btn.png")
    sound_slider_btn = Button(sound_slider_obj.x + sound_slider_obj.width * consts.wS,
                              sound_slider_obj.y + sound_slider_obj.height / 2 - 14, 26, 28,
                              r"buttons\without text\default-slider-btn.png",
                              r"buttons\without text\hover-slider-btn.png",
                              r"buttons\without text\press-slider-btn.png")

    field_video = Object(windows.width // 2 + 15, title.y + 104, 420, 430,
                         fr"objects\{consts.languageNow}\video-field-obj.png")
    fs_name = Object(field_video.x + field_video.width / 2 - 332 / 2, title.y + 226, 332, 75,
                     fr"objects\{consts.languageNow}\fullscreen-obj.png")
    fs_btn = Button(fs_name.x + fs_name.width // 2 - 136 // 2, fs_name.y + fs_name.height + 15, 136, 62,
                    fr"buttons\{consts.languageNow}\default-fullscreen-off-btn.png",
                    rf"buttons\{consts.languageNow}\hover-fullscreen-off-btn.png",
                    fr"buttons\{consts.languageNow}\default-fullscreen-on-btn.png",
                    r"data\sounds\menu-button-sound.mp3", "",
                    "", "", "", "", rf"buttons\{consts.languageNow}\hover-fullscreen-on-btn.png",
                    fr"buttons\{consts.languageNow}\no-active-fullscreen-off-btn.png")
    fs_message = Object(fs_btn.x + fs_btn.width // 2 - 324 / 2, fs_btn.y - 154, 324, 152,
                        fr"objects\{consts.languageNow}\for-starichoks-obj.png")
    fs_message_btn = Button(fs_message.x + fs_message.width // 2 - 106 / 2, fs_message.y + fs_message.height - 66, 106,
                            32,
                            fr"buttons\{consts.languageNow}\default-get-btn.png",
                            fr"buttons\{consts.languageNow}\hover-get-btn.png",
                            fr"buttons\{consts.languageNow}\press-get-btn.png", r"data\sounds\menu-button-sound.mp3")

    langauge_obj = Object(field_video.x + field_video.width / 2 - 216 / 2, title.y + 406, 228, 50,
                          r"objects\rus\language-rus-obj.png", "", r"objects\eng\language-eng-obj.png")
    r_arrow_btn = Button(langauge_obj.x + langauge_obj.width + 15, langauge_obj.y + langauge_obj.height / 2 - 16, 36,
                         40,
                         r"buttons\without text\default-arrow-btn.png", r"buttons\without text\hover-arrow-btn.png",
                         r"buttons\without text\press-arrow-btn.png", r"data\sounds\menu-button-sound.mp3")
    arrow_btn = Button(langauge_obj.x - 36 - 15, langauge_obj.y + langauge_obj.height / 2 - 16, 36, 40,
                       r"buttons\without text\default-r-arrow-btn.png", r"buttons\without text\hover-r-arrow-btn.png",
                       r"buttons\without text\press-r-arrow-btn.png", r"data\sounds\menu-button-sound.mp3")

    tmpCheckS = False
    running = True
    while running:

        windows.screen.blit(consts.menu_bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    transition()
                    menu.main_menu()

            if event.type == pygame.USEREVENT and event.button == cross_btn:
                transition()
                menu.main_menu()

            if event.type == pygame.USEREVENT and event.button == fs_btn:
                if windows.screenChecker:
                    if windows.fullscreen:
                        windows.fullscreen = 0
                        fullscreenChanger(windows.fullscreen)
                        settings_menu()
                    else:
                        windows.fullscreen = 1
                        fullscreenChanger(windows.fullscreen)
                        settings_menu()

            if event.type == pygame.USEREVENT and (event.button == arrow_btn or event.button == r_arrow_btn):
                if consts.languageNow == 'eng':
                    consts.languageNow = 'rus'
                elif consts.languageNow == 'rus':
                    consts.languageNow = 'eng'
                fileManager.languageExport(consts.languageNow)
                settings_menu()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == music_slider_btn:
                consts.isSliderMusic = True

            elif event.type == pygame.MOUSEBUTTONUP and event.button == music_slider_btn:
                consts.isSliderMusic = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == sound_slider_btn:
                consts.isSliderSound = True

            elif event.type == pygame.MOUSEBUTTONUP and event.button == sound_slider_btn:
                consts.isSliderSound = False

            elif event.type == pygame.MOUSEMOTION:
                if consts.isSliderMusic or consts.isSliderSound:
                    volumeChanger(event, music_slider_btn, music_slider_obj, sound_slider_btn, sound_slider_obj)

            elif event.type == pygame.USEREVENT and event.button == fs_message_btn:
                webbrowser.open('https://www.dns-shop.ru/catalog/recipe/7fcb16e8135fbd91/fullhd/')

            for button in [cross_btn, fs_btn, arrow_btn, r_arrow_btn]:
                button.handle_event(event, consts.volS)

            if tmpCheckS:
                fs_message_btn.handle_event(event, consts.volS)

            for slider_button in [music_slider_btn, sound_slider_btn]:
                slider_button.handle_event_slider(event)

        for obj in [title, field_audio, field_video, fs_name, sound_name, music_name, music_slider_obj,
                    sound_slider_obj]:
            obj.draw(windows.screen)

        langauge_obj.drawLanguage(windows.screen, consts.languageNow)

        for button in [cross_btn, music_slider_btn, sound_slider_btn, arrow_btn, r_arrow_btn]:
            button.check_hover(pygame.mouse.get_pos())
            button.draw(windows.screen)

        if windows.screenChecker:
            fs_btn.check_hover(pygame.mouse.get_pos())
        if (pygame.mouse.get_pos()[0] < fs_message.x or pygame.mouse.get_pos()[0] > fs_message.x + fs_message.width
                or pygame.mouse.get_pos()[1] < fs_message.y or pygame.mouse.get_pos()[1] > fs_btn.y + fs_btn.height):
            tmpCheckS = False
        if fs_btn.rect.collidepoint(pygame.mouse.get_pos()) and not windows.screenChecker:
            tmpCheckS = True
        if tmpCheckS:
            fs_message.draw(windows.screen)
            fs_message_btn.check_hover(pygame.mouse.get_pos())
            fs_message_btn.draw(windows.screen)
        fs_btn.draw_f11(windows.screen, windows.fullscreen)

        consts.clock.tick(consts.fps)
        pygame.display.flip()
