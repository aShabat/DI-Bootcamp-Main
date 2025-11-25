import { useState } from "react"
import quotes from "./quotes.js"
function random_index(length, non_repeat = null) {
  const out = Math.floor(length * Math.random())
  if (out === non_repeat) return random_index(length, non_repeat)
  return out
}

const color_digits = "0123456789ABCDEF"
function random_color_digit() {
  return color_digits[random_index(16)]
}

function random_color() {
  return "#" + Array.from(Array(6).keys()).map(_ => random_color_digit()).join("")
}

export default function QuoteGenerator() {
  const [quoteIndex, SetQuoteIndex] = useState(random_index(quotes.length))
  const quote = quotes[quoteIndex]


  const [bgColor, SetBgColor] = useState(random_color())
  const [quoteColor, SetQuoteColor] = useState(random_color())
  const [buttonColor, SetButtonColor] = useState(random_color())

  function onClick() {
    SetQuoteIndex(random_index(quotes.length, quoteIndex))
    SetBgColor(random_color())
    SetQuoteColor(random_color())
    SetButtonColor(random_color())
  }

  return <div style={{ background: bgColor }}>
    <h1 style={{ color: quoteColor }}>"{quote.quote}"</h1>
    <h10>-{quote.author}-</h10>
    <button style={{ background: buttonColor }} onClick={onClick}>Generate</button>
  </div >
}
