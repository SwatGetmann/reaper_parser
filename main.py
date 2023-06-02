from reaper_project import ReaperProject 
        

if __name__ == '__main__':
    print("Welcome to Reaper Parser.")
    
    test_reaper_project_fpath = "d:\\05 Music Lab\\Вдохновения\\Tbilisi Acoustic G\\221012 01 Tbilisi Sunrise\\221012 01 Zoom Rec Again.rpp"
    # test_reaper_project_fpath = "d:\\05 Music Lab\\Вдохновения\\Tbilisi Acoustic G\\230503 three ideas\\230503 three ideas.rpp"
        
    ReaperProject(test_reaper_project_fpath)