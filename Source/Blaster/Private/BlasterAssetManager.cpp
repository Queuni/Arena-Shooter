

#include "BlasterAssetManager.h"

#include "Blaster/BlasterGameplayTags.h"

UBlasterAssetManager::UBlasterAssetManager()
{
}

void UBlasterAssetManager::StartInitialLoading()
{
	Super::StartInitialLoading();

	FBlasterGameplayTags::InitializeNativeTags();
}
