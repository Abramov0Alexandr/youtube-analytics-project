from src.video import Video

if __name__ == '__main__':
    broken_video = Video('broken_video_id')
    assert broken_video.title is None
    assert broken_video.like_count is None


# Пример работы программы в случае, если id видео передано корректно

    video1 = Video('9lO06Zxhu88')  # '9lO06Zxhu88' - это id видео из ютуб

    assert video1.video_url == 'https://www.youtube.com/watch?v=9lO06Zxhu88'
    assert video1.video_id == '9lO06Zxhu88'
    assert video1.title == 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)'
    assert video1.like_count == '976862'
    assert video1.view_count == '49458251'
    assert str(video1) == 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)'
