

#include "HUD/BTeamSelectPlayerEntry.h"

#include "Components/TextBlock.h"

void UBTeamSelectPlayerEntry::SetName(const FString& Name)
{
	if(PlayerName)
	{
		PlayerName->SetText(FText::FromString(Name));
	}
}
