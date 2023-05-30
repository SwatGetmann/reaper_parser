from xml.dom.minidom import parse

if __name__ == '__main__':
    print("Welcome to Reaper Parser.")
    
    test_reaper_project_fpath = "d:\\05 Music Lab\\Вдохновения\\Tbilisi Acoustic G\\221012 01 Tbilisi Sunrise\\221012 01 Zoom Rec Again.rpp"
    
    dom1 = parse(test_reaper_project_fpath)
    
    print(dom1)