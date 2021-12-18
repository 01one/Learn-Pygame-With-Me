import pygame,sys
from pygame.locals import*
pygame.init()
clock=pygame.time.Clock()
screen_width=600
screen_height=600
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Poems from heart")


white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)
image=pygame.image.load('background.png')
image2=pygame.image.load('icon.jpg')
pygame.display.set_icon(image2)

text_h=1200
n=0
poems=["Twinkle, Twinkle, Little Star\nBY JANE TAYLOR\n\nTwinkle, twinkle, little star,\nHow I wonder what you are!\nUp above the world so high,\nLike a diamond in the sky.\n\nWhen the blazing sun is gone,\nWhen he nothing shines upon,\nThen you show your little light,\nTwinkle, twinkle, all the night.\n\nThen the traveler in the dark\nThanks you for your tiny spark,\nHow could he see where to go,\nIf you did not twinkle so?\nIn the dark blue sky you keep,\nOften through my curtains peep\nFor you never shut your eye,\nTill the sun is in the sky.\n\nAs your bright and tiny sparkn\nLights the traveler in the dark,\nThough I know not what you are,\nTwinkle, twinkle, little star.","I Remember, I Remember\nBY THOMAS HOOD\n\nI remember, I remember,\nThe house where I was born,\nThe little window where the sun\nCame peeping in at morn;\nHe never came a wink too soon,\nNor brought too long a day,\nBut now, I often wish the night\nHad borne my breath away!\n\nI remember, I remember,\nThe roses, red and white,\nThe vi'lets, and the lily-cups,\nThose flowers made of light!\nThe lilacs where the robin built,\nAnd where my brother set\nThe laburnum on his birthday,—\nThe tree is living yet!\n\nI remember, I remember,\nWhere I was used to swing,\nAnd thought the air must rush as fresh\nTo swallows on the wing;\nMy spirit flew in feathers then,\nThat is so heavy now,\nAnd summer pools could hardly cool\nThe fever on my brow!\n\nI remember, I remember,\nThe fir trees dark and high;\nI used to think their slender tops\nWere close against the sky:\nIt was a childish ignorance,\nBut now 'tis little joy\nTo know I'm farther off from heav'n\nThan when I was a boy.","I Love You\nBY ELLA WHEELER WILCOX\n\nI love your lips when they’re wet with wine\nAnd red with a wild desire;\nI love your eyes when the lovelight lies\nLit with a passionate fire.\nI love your arms when the warm white flesh\nTouches mine in a fond embrace;\nI love your hair when the strands enmesh\nYour kisses against my face.\n\nNot for me the cold, calm kiss\nOf a virgin’s bloodless love;\nNot for me the saint’s white bliss,\nNor the heart of a spotless dove.\nBut give me the love that so freely gives\nAnd laughs at the whole world’s blame,\nWith your body so young and warm in my arms,\nIt sets my poor heart aflame.\n\nSo kiss me sweet with your warm wet mouth,\nStill fragrant with ruby wine,\nAnd say with a fervor born of the South\nThat your body and soul are mine.\nClasp me close in your warm young arms,\nWhile the pale stars shine above,\nAnd we’ll live our whole young lives away\nIn the joys of a living love.","To the Virgins, to Make Much of Time\nBY ROBERT HERRICK\n\nGather ye rose-buds while ye may,\nOld Time is still a-flying;\nAnd this same flower that smiles today\nTomorrow will be dying.\n\nThe glorious lamp of heaven, the sun,\nThe higher he’s a-getting,\nThe sooner will his race be run,\nAnd nearer he’s to setting.\n\nThat age is best which is the first,\nWhen youth and blood are warmer;\nBut being spent, the worse, and worst\nTimes still succeed the former.\n\nThen be not coy, but use your time,\nAnd while ye may, go marry;\nFor having lost but once your prime,\nYou may forever tarry.","O Me! O Life!\nBY WALT WHITMAN\n\nOh me! Oh life! of the questions of these recurring,\nOf the endless trains of the faithless, of cities fill’d with the foolish,\nOf myself forever reproaching myself, (for who more foolish than I, and who more faithless?)\nOf eyes that vainly crave the light, of the objects mean, of the struggle ever renew’d,\nOf the poor results of all, of the plodding and sordid crowds I see around me,\nOf the empty and useless years of the rest, with the rest me intertwined,\nThe question, O me! so sad, recurring—What good amid these, O me, O life?\n\n                                  Answer.\nThat you are here—that life exists and identity,\nThat the powerful play goes on, and you may contribute a verse.","All the world’s a stage\nBY WILLIAM SHAKESPEARE\n\nAll the world’s a stage,\nAnd all the men and women merely players;\nThey have their exits and their entrances;\nAnd one man in his time plays many parts,\nHis acts being seven ages. At first the infant,\nMewling and puking in the nurse’s arms;\nAnd then the whining school-boy, with his satchel\nAnd shining morning face, creeping like snail\nUnwillingly to school. And then the lover,\nSighing like furnace, with a woeful ballad\nMade to his mistress’ eyebrow. Then a soldier,\nFull of strange oaths, and bearded like the pard,\nJealous in honour, sudden and quick in quarrel,\nSeeking the bubble reputation\nEven in the cannon’s mouth. And then the justice,\nIn fair round belly with good capon lin’d,\nWith eyes severe and beard of formal cut,\nFull of wise saws and modern instances;\nAnd so he plays his part. The sixth age shifts\nInto the lean and slipper’d pantaloon,\nWith spectacles on nose and pouch on side; \nHis youthful hose, well sav’d, a world too wide\nFor his shrunk shank; and his big manly voice,\nTurning again toward childish treble, pipes\nAnd whistles in his sound. Last scene of all,\nThat ends this strange eventful history,\nIs second childishness and mere oblivion;\nSans teeth, sans eyes, sans taste, sans everything.","A Psalm of Life\nBY HENRY WADSWORTH LONGFELLOW\n\nTell me not, in mournful numbers,\n   Life is but an empty dream!\nFor the soul is dead that slumbers,\n   And things are not what they seem.\n\nLife is real! Life is earnest!\n   And the grave is not its goal;\nDust thou art, to dust returnest,\n   Was not spoken of the soul.\n\nNot enjoyment, and not sorrow,\n   Is our destined end or way;\nBut to act, that each to-morrow\n   Find us farther than to-day.\n\nArt is long, and Time is fleeting,\n   And our hearts, though stout and brave,\nStill, like muffled drums, are beating\n   Funeral marches to the grave.\n\nIn the world’s broad field of battle,\n   In the bivouac of Life,\nBe not like dumb, driven cattle!\n   Be a hero in the strife!\n\nTrust no Future, howe’er pleasant!\n   Let the dead Past bury its dead!\nAct,— act in the living Present!\n   Heart within, and God o’erhead!\n\nLives of great men all remind us\n   We can make our lives sublime,\nAnd, departing, leave behind us\n   Footprints on the sands of time;\n\nFootprints, that perhaps another,\n   Sailing o’er life’s solemn main,\nA forlorn and shipwrecked brother,\n   Seeing, shall take heart again.\n\nLet us, then, be up and doing,\n   With a heart for any fate;\nStill achieving, still pursuing,\n   Learn to labor and to wait.","The Road Not Taken\nBY ROBERT FROST\n\nTwo roads diverged in a yellow wood,\nAnd sorry I could not travel both\nAnd be one traveler, long I stood\nAnd looked down one as far as I could\nTo where it bent in the undergrowth;\n\nThen took the other, as just as fair,\nAnd having perhaps the better claim,\nBecause it was grassy and wanted wear;\nThough as for that the passing there\nHad worn them really about the same,\n\nAnd both that morning equally lay\nIn leaves no step had trodden black.\nOh, I kept the first for another day!\nYet knowing how way leads on to way,\nI doubted if I should ever come back.\n\nI shall be telling this with a sigh\nSomewhere ages and ages hence:\nTwo roads diverged in a wood, and I—\nI took the one less traveled by,\nAnd that has made all the difference."]
def text_view(text_color,text,text_font,text_rect):
    text_lines = []
    splited_lines =text.splitlines()
    for splited_line in splited_lines:
        if text_font.size(splited_line)[0] > text_rect.width:
            words = splited_line.split(' ')
            for word in words:
                if text_font.size(word)[0] >= text_rect.width:
                    pass
            fitted_line = ""
            for word in words:
                test_line = fitted_line + word + " "  
                if text_font.size(test_line)[0] < text_rect.width:
                    fitted_line = test_line
                else:
                    text_lines.append(fitted_line)
                    fitted_line = word + " "
            text_lines.append(fitted_line)
        else:
            text_lines.append(splited_line)
    surface = pygame.Surface(text_rect.size)
    surface.blit(image,(0,0))
    
    
    text_raw = 0
    for line in text_lines:
        if text_raw + text_font.size(line)[1] >= text_rect.height:
            pass
        if line != "":
            text_surface = text_font.render(line, 1, text_color)
            surface.blit(text_surface, (0, text_raw))
        text_raw +=text_font.size(line)[1]
    return surface
    
scroll=0

game_running=True
while game_running:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
		if event.type == MOUSEWHEEL:
			#print(event)
			if event.y<0:
				if scroll>=-text_h+600:
					scroll-=30
			elif event.y>0:
				if scroll<=0:
					scroll+=30
		if event.type==pygame.MOUSEBUTTONDOWN:
			if event.button==1:
				n+=1
				if n>7:
					n=0
				scroll=0
			if event.button==3:
				n-=1
				if n<-7:
					n=0
				scroll=0	
	if n==0:
		text_h=800
	elif n==-1 or n==7:
		text_h=800
	elif n==-2 or n==6:
		text_h=1430
		
	elif n==-3 or n==5:
		text_h=950
	elif n==-4 or n==4:
		text_h=720
	elif n==-5 or n==3:
		text_h=700
	elif n==-6 or n==2:
		text_h=900
	elif n==-7 or n==1:
		text_h=1200
		
		
	Text_color=black
	Text_font=pygame.font.Font('Roboto-Regular.ttf',25)
	Text_rect=pygame.Rect(20,scroll,screen_width,text_h)
	show_text=text_view(Text_color,poems[n],Text_font,Text_rect)
	screen.blit(image,(0,0))
	screen.blit(show_text, Text_rect)
	pygame.display.update()
