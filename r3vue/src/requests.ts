import type { Video } from "./types"

class Requests {
    static async getVideos(ipAddress: string) {
        const response = await fetch(`http://${ipAddress}:5000/videos`)

        return  await response.json()
    }

    static async getVideo(ipAddress: string, video: Video) {
        const response = await fetch(
            `http://${ipAddress}:5000/videos/${video.id}`,
        )
        return await response.json()
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
