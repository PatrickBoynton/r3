import type { Video } from "./types"

class Requests {
    static async getVideos(ipAddress: string) {
        const videoList: Video[] = []
        const response = await fetch(`http://${ipAddress}:5000/videos`)
        const vids = await response.json()

        vids.forEach((video: Video) => {
            videoList.push(video)
        })

        return videoList
    }

    static async getVideo(ipAddress: string, video: Video, emit?: any) {
        const response = await fetch(
            `http://${ipAddress}:5000/videos/${video.id}`,
        )
        const sv = await response.json()
        emit("getVideo", sv)
        return sv
    }

    static async getRandomVideo(ipAddress: string, query?: string) {
        const response = await fetch(
            `http://${ipAddress}:5000/videos/random${query}`,
        )

        return await response.json()
    }

    static async getVideoContext(ipAddress: string) {
        try {
            const response = await fetch(
                `http://${ipAddress}:5000/video-context`,
            )
            return await response.json()
        } catch (error) {
            console.error("No context.")
        }
    }

    static async deleteVideoStatus(ipAddress: string) {
        await fetch(`http://${ipAddress}:5000/videos`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
        })
    }

    static async updateVideo(ipAddress: string, video: Video) {
        await fetch(`http://${ipAddress}:5000/videos/${video.id}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(video),
        })
    }
}

export default Requests
