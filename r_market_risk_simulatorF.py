"""Rhinehart Financial Risk Advisor.

This beginner-friendly program shows a simple intro screen,
lets the user choose one of three business prompts,
and then estimates the investment risk from 0 to 100.
"""

import random


def print_intro():
    """Display the opening screen with a bold-style title."""
    print("\n==============================")
    print("RHINEHART FINANCIAL RISK ADVISOR")
    print("==============================")
    print("Welcome to your beginner-friendly investment risk assistant.")
    print("A new financial-risk scenario will be generated for you each round.\n")


def generate_prompt():
    """Generate a new financial-risk scenario with random values and names."""
    prompt_templates = [
        "A local bakery is preparing to expand into a new city with a larger storefront and more equipment to better serve its customers.",
        "A small clothing store is considering a new website and online inventory system to support growth in a competitive market.",
        "A delivery company is planning to hire more drivers during a slower economy in hopes of meeting demand and strengthening operations.",
        "A coffee shop is thinking about opening a second location in a different neighborhood.",
        "A software startup is preparing to launch a new product in a fast-changing industry.",
    ]

    names = ["Carter", "Wesley", "Jordan", "Taylor", "Morgan", "Avery", "Riley", "Casey", "Allie"]
    person_name = random.choice(names)

    if person_name not in {"Carter", "Wesley"}:
        person_name = random.choice(["Carter", "Wesley", person_name])

    interest_rate = round(random.uniform(2, 12), 2)
    unemployment_rate = round(random.uniform(3, 15), 2)
    business_capital = random.randint(15000, 60000)
    investment_cost = random.randint(5000, business_capital - 1000)
    market_demand = random.choice(["high", "medium", "low"])
    competition = random.choice(["low", "medium", "high"])

    prompt = (
        f"{person_name} is the investor and business owner reviewing this opportunity. "
        f"{random.choice(prompt_templates)} "
        f"The business is weighing whether this decision is the right move for long-term growth."
    )

    return (
        prompt,
        interest_rate,
        unemployment_rate,
        business_capital,
        investment_cost,
        market_demand,
        competition,
    )


def calculate_risk_score(interest_rate, unemployment_rate, business_capital, investment_amount, market_demand, competition):
    """Turn the scenario into a simple risk score from 0 to 100."""
    score = (interest_rate * 2.5) + (unemployment_rate * 2)

    if investment_amount < business_capital / 2:
        score += 2
    else:
        score += 10

    if market_demand == "low":
        score += 12
    elif market_demand == "medium":
        score += 6
    else:
        score -= 3

    if competition == "high":
        score += 12
    elif competition == "medium":
        score += 6
    else:
        score -= 3

    if score > 100:
        return 100
    if score < 0:
        return 0
    return round(score)


def get_risk_level(score):
    """Convert the score into a simple label."""
    if score <= 33:
        return "Low"
    if score <= 66:
        return "Medium"
    return "High"


def evaluate_answers(decision_answer, user_level, risk_level):
    """Check whether the user's YES/NO and risk-level answers match the scenario."""
    if risk_level == "Low":
        accepted_levels = {"LOW RISK"}
        decision_correct = decision_answer == "YES"
    elif risk_level == "Medium":
        accepted_levels = {"MEDIUM RISK", "LOW RISK", "HIGH RISK"}
        decision_correct = True
    else:
        accepted_levels = {"HIGH RISK"}
        decision_correct = decision_answer == "NO"

    level_correct = user_level.upper() in {level.upper() for level in accepted_levels}
    return decision_correct, level_correct


def explain_decision(business_capital, investment_cost, market_demand, competition, risk_level, risk_score):
    """Explain whether the investment looks safe or unsafe based on the selected factors."""
    print("\nContinue with investment?")
    answer = input("Enter YES or NO: ").strip().upper()

    if answer not in {"YES", "NO"}:
        print("Please enter YES or NO.")
        return

    user_level = input("Do you think this investment has LOW RISK, MEDIUM RISK, or HIGH RISK? ").strip().upper()

    if user_level in {"LOW", "LOW RISK"}:
        normalized_user_level = "LOW RISK"
    elif user_level in {"MEDIUM", "MEDIUM RISK"}:
        normalized_user_level = "MEDIUM RISK"
    else:
        normalized_user_level = "HIGH RISK"
    decision_correct, level_correct = evaluate_answers(answer, normalized_user_level, risk_level)
    level_description = "correct" if level_correct else "incorrect"

    print("\nYour answers:")
    print(f"- Investment decision: {answer.lower()}")
    print(f"- Risk level estimate: {normalized_user_level.lower()}")

    print("\nRisk level evaluation:")
    if level_correct:
        print(f"Your risk level of {normalized_user_level.lower()} was correct.")
    else:
        print(f"Your risk level of {normalized_user_level.lower()} was incorrect. The actual risk level was {risk_level.lower()}.")

    if decision_correct:
        print(f"Your YES/NO choice was correct.")
    else:
        better_choice = "YES" if risk_level == "Low" else "NO"
        print(f"Your YES/NO choice was incorrect. The better choice was {better_choice} because the actual risk level was {risk_level.lower()}.")

    if market_demand == "high":
        demand_description = "demand is strong and sustained, creating a favorable environment for converting the opportunity into revenue"
    elif market_demand == "medium":
        demand_description = "demand is moderate, so the business should be cautious and cannot rely on robust customer interest"
    else:
        demand_description = "demand is weak, which makes it difficult to generate meaningful sales from the opportunity"

    if competition == "low":
        competition_description = "few competitors are present, improving the business’s ability to differentiate and capture market share"
    elif competition == "medium":
        competition_description = "the space is moderately contested, requiring the business to sharpen its value proposition to stand out"
    else:
        competition_description = "the market is crowded with established players, making customer acquisition and momentum much harder"

    if investment_cost < business_capital / 2:
        capital_description = "the investment is a relatively conservative allocation, preserving the business’s financial flexibility"
    else:
        capital_description = "the investment consumes a substantial portion of capital, reducing the company’s ability to absorb setbacks"

    if answer == "YES":
        if risk_level == "Low":
            print(
                f"{answer} is a reasonable choice because business capital of ${business_capital:,} gives the business room to handle the plan. "
                f"Investment cost of ${investment_cost:,} means {capital_description}. "
                f"Market demand is {market_demand}, which means {demand_description}. "
                f"Competition is {competition}, which means {competition_description}. "
                f"Taken together, these factors make the investment feel more manageable and safer."
            )
        else:
            print(
                f"{answer} is riskier because business capital of ${business_capital:,} leaves less room for error if the plan underperforms. "
                f"Investment cost of ${investment_cost:,} means {capital_description}. "
                f"Market demand is {market_demand}, which means {demand_description}. "
                f"Competition is {competition}, which means {competition_description}. "
                f"When the business spends too much of its capital in a weak or crowded market, the venture becomes harder to justify."
            )
    elif answer == "NO":
        if risk_level == "Low":
            print(
                f"{answer} is not necessary because business capital of ${business_capital:,} gives the business enough flexibility to support the opportunity. "
                f"Investment cost of ${investment_cost:,} means {capital_description}. "
                f"Market demand is {market_demand}, which means {demand_description}. "
                f"Competition is {competition}, which means {competition_description}. "
                f"Because the cost is manageable and the market conditions are not too discouraging, the investment looks reasonable to continue."
            )
        else:
            print(
                f"{answer} is a sensible choice because business capital of ${business_capital:,} leaves the business with less room to absorb losses. "
                f"Investment cost of ${investment_cost:,} means {capital_description}. "
                f"Market demand is {market_demand}, which means {demand_description}. "
                f"Competition is {competition}, which means {competition_description}. "
                f"When the cost is high and the market is weak or crowded, the investment becomes too risky."
            )

    print("\nOverall Risk Assessment:")
    print(f"- Risk Level: {risk_level}")
    print(f"- Your risk level was {level_description}.")


def main():
    """Run the simulator and show the result."""
    while True:
        print_intro()
        prompt, interest_rate, unemployment_rate, business_capital, investment_cost, market_demand, competition = generate_prompt()

        print("\nScenario Overview")
        print("-----------------")
        print(prompt)

        print("\nStatistics:")
        print(f"- Business Capital: ${business_capital:,}")
        print(f"- Investment Cost: ${investment_cost:,}")
        print(f"- Market Demand: {market_demand}")
        print(f"- Competition: {competition}")

        risk_score = calculate_risk_score(
            interest_rate,
            unemployment_rate,
            business_capital,
            investment_cost,
            market_demand,
            competition,
        )
        risk_level = get_risk_level(risk_score)

        explain_decision(
            business_capital,
            investment_cost,
            market_demand,
            competition,
            risk_level,
            risk_score,
        )

        print("\nWould you like to generate a new question?")
        continue_choice = input("Enter YES for a new question or NO to exit: ").strip().upper()
        if continue_choice != "YES":
            break


if __name__ == "__main__":
    main()
