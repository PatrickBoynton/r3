import type { Video, VideoContext } from "./types"

class Requests {
    static async getVideos(ipAddress: string): Promise<Video[]> {
        const response = await fetch(`http://${ipAddress}:5001/videos`)

        return await response.json()
    }

    static async getVideo(ipAddress: string, video: Video): Promise<Video> {
        const response = await fetch(
            `http://${ipAddress}:5001/videos/${video.id}`,
        )
        return await response.json()
    }

    static async getRandomVideo(
        ipAddress: string,
        query?: string,
    ): Promise<Video> {
        const response = await fetch(
            `http://${ipAddress}:5001/videos/random${query}`,
        )

        return await response.json()
    }

    static async getNewRandomVideo(ipAddress: string, query?: string): Promise<Video> {
        let response;
        if(query) {
            response = await fetch(
            `http://${ipAddress}:5001/videos/random/new${query}`,
        )

        } else {
            response = await fetch(
            `http://${ipAddress}:5001/videos/random/new`,
        )
        }

        return await response.json()
    }

    static async getVideoContext(
        ipAddress: string,
    ): Promise<VideoContext | undefined> {
        try {
            const response = await fetch(
                `http://${ipAddress}:5001/video-context`,
            )
            return await response.json()
        } catch (error) {
            console.error("No context.")
        }
    }

    static async deleteVideoStatus(ipAddress: string) {
        await fetch(`http://${ipAddress}:5001/videos`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
        })
    }

    static async resetPlayCount(ipAddress: string) {
        await fetch(`http://${ipAddress}:5001/videos`, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json'
            }
        })
    }

    static async updateVideo(ipAddress: string, video: Video) {
        await fetch(`http://${ipAddress}:5001/videos/${video.id}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(video),
        })
    }

    static async uploadVideo(formData: FormData) {
        await fetch('http://localhost:5001/videos/upload', {
            method: 'POST',
            body: formData,
        })
    }
}

export default Requests
