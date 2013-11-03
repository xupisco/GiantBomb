## UNDER MIT LICENSE

Copyright (C) 2011-2012 Leandro Voltolino <xupisco@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


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
 * getFranchise(franchise_id)
 * getFranchises(offset)
 
*Everything returns an object:*  

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
