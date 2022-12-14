from fileinput import filename
import re
#"(1992) (TV Episode) - Season 4 | Episode 2 - The Simpsons (1989) (TV Series)"

def getYearFromDescription(desc):
    regex = re.search('([0-9]+)', desc)
    return regex.group(0)

def getEpisodeCodeFromDescription(desc):
    regex = re.search('-(.*)-', desc)
    try:
        numbers = (regex.group(1)).split(" | ")
        
        season_number_regex= re.search('[0-9]+', numbers[0])
        season_number = append0IfLessThan10(season_number_regex.group(0))

        episode_number_regex = re.search('[0-9]+', numbers[1])
        episode_number = append0IfLessThan10(episode_number_regex.group(0))

        episode_code = f"s{season_number}e{episode_number}"

        return episode_code
    except:
        return ""

def getSeriesTitleFromDescription(desc):
    print("desc: " + desc)
    regex = None
    regex = re.search('- (.*) \([0-9]+\)', desc)
    return regex.group(1)

def getFileExtension(fileName):
    return "." + fileName.rsplit(".", 1)[1]

def removeFileExtension(fileName):
    return fileName.rsplit(".", 1)[0]

def append0IfLessThan10(number):
    numString = number.lstrip('0')
    numAsInt = int(numString)
    return f"0{numString}" if numAsInt < 10 else numString

def getSeasonNumber(number):
    regex = re.search('.*?([0-9]+).*', number)
    print(regex)
    number = (regex.group(1))
    
    return "Season " + append0IfLessThan10(number)

def hasNumber(text):
    matches = re.findall('\d+', text)
    return len(matches) > 0