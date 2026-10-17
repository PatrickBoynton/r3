export type Video = {
    id: string
    title: string
    url: string
    image?: string
    duration: number
    uploaded_date: Date
    video_status: VideoStatus
    category: Category
    tags: [Tag]
}

type VideoStatus = {
    id: string
    played: boolean
    current_play_time: number
    play_count: number
    selection_count: number
    is_watch_later: boolean
    last_played: Date | null
}

export type VideoContext = {
    id: string
    current_video: Video
    total_videos: number
    video_plays: number
    current_os: string
}

export type Tag = {
    id: string
    name: string
}

export type Category = {
    id: string
    name: string
}
