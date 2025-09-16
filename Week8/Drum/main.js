function sound_info(name, key) {
  return { name: name, key: key, audio: null };
}

const sounds = [
  sound_info("boom", "a"),
  sound_info("clap", "s"),
  sound_info("hihat", "d"),
  sound_info("kick", "f"),
  sound_info("openhat", "g"),
  sound_info("ride", "h"),
  sound_info("snare", "j"),
  sound_info("tink", "k"),
  sound_info("tom", "l"),
];

function play_sound(sound) {
  if (sound.audio === null) {
    sound.audio = new Audio("./sounds/" + sound.name + ".wav");
  }
  sound.audio.currentTime = 0;
  sound.audio.play();
}

for (const sound of sounds) {
  window.addEventListener("keydown", (e) => {
    if (e.key === sound.key) {
      play_sound(sound);
    }
  });

  const button = document.getElementById(sound.name);
  button.addEventListener("click", () => {
    play_sound(sound);
  });
}
