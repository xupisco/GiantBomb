## Python wrapper for Giantbomb API!

**Get your API Key at http://api.giantbomb.com**

Basic usage:  

    import giantbomb  
    gb = giantbomb.Api('YOUR_KEY')
    
**Current Methods:**  

 * search(str, offset)
 * getGame(game_id)
 * getGames(platform_id, offset)
 * getVideo(video_id)
 * getPlatform(platform_id)
 * getPlatforms(offset)
 
*Everything return an object:*  

**Examples:**  

    import giantbomb  
    gb = giantbomb.Api('YOUR_KEY')  
    
    games = gb.getGames(94, 12300) // 94 = PC
    print games
    
    >>> [<29220: Zero Gear>, <29234: Pro Cycling Manager: Season 2010>,
         <29238: Allods Online>, <29240: Hammerfight>, <29247: Sacraboar>,
         <29249: POWDER>, <29257: Grand Fantasia>, ...]
    
    ------------------------------------------------------------------------------
    
    results = gb.search('call of duty')
    print results
    
    >>> [<26423: Call of Duty: Black Ops>, <2133: Call of Duty 4: Modern Warfare>,
         <20777: Call of Duty: World at War>, ...]
    
    game = gb.getGame(26423) // or gb.getGame(results[0])
    for p in game.platforms:
        print p.name
        
    >>> PlayStation 3
        Wii
        Nintendo DS
        PlayStation Network (PS3)
        Xbox 360
        PC

Yep, that's it!  
Hugs!