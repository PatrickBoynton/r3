export const formatDate = (date: Date) =>
    new Date(String(date).split("T")[0] as string).toDateString()

export const convertToPlayTime = (time: number) => {
    const dateObj = new Date(time * 1000)
    const hours = dateObj.getUTCHours()
    const minutes = dateObj.getUTCMinutes()
    const seconds = dateObj.getUTCSeconds()
    const timeString = `${hours.toString().padStart(2, "0")}:${minutes.toString().padStart(2, "0")}:${seconds.toString().padStart(2, "0")}`

    return timeString
}
