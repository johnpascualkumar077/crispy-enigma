function htmlDecode(input) {
  const doc = new DOMParser().parseFromString(input, "text/html");
  return doc.documentElement.textContent;
}

// 使用例
const encodedString = "&lt;div&gt;Hello &amp; World!&lt;/div&gt;";
const decodedString = htmlDecode(encodedString);
console.log(decodedString); // <div>Hello & World!</div>
