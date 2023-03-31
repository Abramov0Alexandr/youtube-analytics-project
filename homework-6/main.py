from src.video import Video

if __name__ == '__main__':
    broken_video = Video('broken_video_id')
    assert broken_video.title is None
    assert broken_video.like_count is None


# Пример работы программы в случае, если id видео передано корректно
    video1 = Video('9lO06Zxhu88')  # '9lO06Zxhu88' - это id видео из ютуб
    assert str(video1.video_url)
    assert str(video1.video_id)
    assert str(video1.title)
    assert str(video1.like_count)
    assert str(video1.view_count)
