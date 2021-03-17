export type Language = "se" | "en";

interface TranslateOptions {
  query: string;
  from: Language;
  to: Language;
}

export async function translate({
  query,
  from,
  to,
}: TranslateOptions): Promise<string | null> {
  console.log({ query, from, to });
  // TODO: Scrape Google and Wikipedia
  return "Fotboll är roligt";
}
